from django.contrib import admin
from .models import Feed

from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
# Register your models here.

admin.site.register(Feed)



class MyAdminSite(AdminSite):
    site_header = 'Event Manager administration'
    site_title = 'Event Manager admin'

    login_template = 'admin/login.html'


admin_site = MyAdminSite(name='myadmin')

admin_site.register(User)
admin_site.register(Group)
