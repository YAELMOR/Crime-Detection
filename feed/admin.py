from django.contrib import admin
from .models import Feed

from django.contrib.auth.models import User, Group
from django.contrib.admin import AdminSite
# Register your models here.

admin.site.register(Feed)


