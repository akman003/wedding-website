from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rsvps.models import Invitee, RSVPLog
from rsvps.serializers import InviteeSerializer
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET'])
def invitee_search(request, query, format=None):
	"""
	Return a list of invitees who match a query
	"""
	invitees = Invitee.objects.filter(name__icontains=query)[:10]
	serializer = InviteeSerializer(invitees, many=True)
	return Response(serializer.data)

@api_view(['GET', 'POST'])
def invitee_detail(request, pk, format=None):
	"""
	Return a specific invitee, with optional update
	"""
	try:
		invitee = Invitee.objects.get(pk=pk)
	except Invitee.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		serializer = InviteeSerializer(invitee)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = InviteeSerializer(invitee, data=request.DATA)
		if serializer.is_valid():
			if invitee.num_rsvpd > invitee.num_allowed:
				return Response("{detail:'Can\'t RSVP more than allowed'}", status=status.HTTP_400_BAD_REQUEST)
			
			# track that this came in, whether they declined or not
			invitee.was_submitted=True
			
			# save a new log entry, in case there is tomfoolery, we can recover:
			
			# get the IP address (need to do something special on webfaction):
			ip_address = request.META['REMOTE_ADDR']

			if 'HTTP_X_FORWARDED_FOR' in request.META:
				ip_address = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()

			l = RSVPLog(invitee=invitee, ip_address=ip_address, num_rsvpd=invitee.num_rsvpd)
			l.save()
			# save the object itself
			serializer.save()
			if settings.SEND_NOTIFICATION:
				# send email notification
				message = invitee.name + ' just RSVPd ' + str(invitee.num_rsvpd) + ' people'
				# fill in your own email addresses here, then uncomment this line
				# (or, even better, put them in your settings.py file :D)
				# send_mail('New Wedding RSVP', message, 'sender@email.com', ['recipient1@gmail.com', 'recipient2@gmail.com'], fail_silently=settings.DEBUG)

			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



