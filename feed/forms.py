from django import forms
from .models import Feed
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class DocumentForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #class Meta:
     #   model = Feed
      #  fields = ('description', 'document', )
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']