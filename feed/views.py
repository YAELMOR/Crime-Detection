from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import *
from pusher import Pusher
import json
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegisterForm

# Create your views here.




#instantiate pusher
pusher = Pusher(app_id=u'1016898', key=u'83b628eba8a1e56d9197', secret=u'18f0d5484a051978b1dc', cluster=u'ap2')
# Create your views here.
# function that serves the welcome page
def index(request):
    # get all current photos ordered by the latest
    all_documents = Feed.objects.all().order_by('-id')
    # return the index.html template, passing in all the feeds
    return render(request, 'index.html', {'all_documents': all_documents})

def pusher_authentication(request):
    channel = request.GET.get('channel_name', None)
    socket_id = request.GET.get('socket_id', None)
    auth = pusher.authenticate(
      channel = channel,
      socket_id = socket_id
    )
 
    return JsonResponse(json.dumps(auth), safe=False)

#function that triggers the pusher request
def push_feed(request):
    # check if the method is post
    if request.method == 'POST':
        # try form validation
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            # trigger a pusher request after saving the new feed element 
            pusher.trigger(u'private-a_channel', u'an_event', {u'description': f.description, u'document': f.document.url})
            return HttpResponse('ok')
        else:
            # return a form not valid error
            return HttpResponse('form not valid')
    else:
       # return error, type isnt post
       return HttpResponse('error, please try again')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html', {'form': form})

