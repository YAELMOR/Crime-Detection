from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Crime administration'
    site_title = 'Crime admin'

    login_template = 'admin/login.html'


admin_site = MyAdminSite(name='myadmin')

admin_site.register(User)
admin_site.register(Group)
