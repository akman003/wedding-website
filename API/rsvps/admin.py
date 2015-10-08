from django.contrib import admin
from rsvps.models import Invitee, RSVPLog

class RSVPLogInline(admin.StackedInline):
	model = RSVPLog
	extra = 0

class InviteeAdmin(admin.ModelAdmin):
	list_display = ('name', 'num_allowed', 'was_submitted', 'num_rsvpd')
	inlines = [RSVPLogInline]

class RSVPLogAdmin(admin.ModelAdmin):
	list_display = ('invitee','ip_address','num_rsvpd','timestamp')

admin.site.register(Invitee, InviteeAdmin)
admin.site.register(RSVPLog, RSVPLogAdmin)
