from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your views here.


class Feed(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='static/documents/')

