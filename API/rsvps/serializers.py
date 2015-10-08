from rsvps.models import Invitee, RSVPLog
from rest_framework import serializers

class InviteeSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Invitee
		fields = ('id', 'name', 'num_allowed', 'num_rsvpd')
		read_only_fields = ('id', 'name', 'num_allowed')
		write_only_fields = ('num_rsvpd',)
