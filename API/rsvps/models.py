from django.db import models
from django.core.validators import MinValueValidator

class Invitee(models.Model):
	name = models.CharField(max_length=200)
	num_allowed = models.IntegerField('Num Invited', validators=[MinValueValidator(0)])
	was_submitted = models.BooleanField('Has RSVPd', default=False)
	num_rsvpd = models.IntegerField('Num RSVPd', default=0, validators=[MinValueValidator(0)])

	def __unicode__(self):
		return self.name

class RSVPLog(models.Model):
	invitee = models.ForeignKey(Invitee)
	ip_address = models.CharField(max_length=200)
	num_rsvpd = models.IntegerField()
	timestamp = models.DateTimeField('Date Submitted', auto_now=True)

	class Meta:
		ordering = ["-timestamp"]
