from django.contrib import admin
from ovpn.models import Team, Member, Route

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
    # pass

class MemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'desc')
    # pass

class RouteAdmin(admin.ModelAdmin):
	list_display = ('subnet', 'desc')
    # pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Route, RouteAdmin)

admin.site.site_header = "VPN Data Management"