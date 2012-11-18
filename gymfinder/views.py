import requests
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from gymfinder.models import *
from gymfinder.helpers import get_lat_lng
from django.contrib.auth.decorators import login_required
from popingym import settings

def login(request):
    return render(request, 'login.html', {} )

@login_required
def get_fb_feed(request, code=None):
        params = {
            'code': code,
            'client_id': settings.SINGLY_CLIENT_ID,
            'client_secret': settings.SINGLY_CLIENT_SECRET
        }
        response = requests.post('https://api.singly.com/services/facebook/feed', data=params)
        if response.status_code == 200:
            objs = json.loads(request.POST)

            for o in objs:
                record = Message(user=request.user, message_id = o.id, message = o.message)
                record.save()
        return HttpResponseRedirect('/show_feed/')

@login_required
def show_feed(request):
    feed = Message.objects.filter(user=request.user)
    return render(request, 'feed.html', {'feed' : feed })

def map(request):
    locations = Location.objects.all()
    return render(request, 'map.html', {'locations':locations })

def loc(request):
    if request.method == 'POST': # If the form has been submitted...
        location_form = LocationForm(request.POST)
        if location_form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            address = location_form.cleaned_data['address']
            latlng = get_lat_lng(address)
            location = Location(address=address, latlng=latlng)
            location.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        location_form = LocationForm() # An unbound form

    return render(request, 'loc.html', { 'location_form' : location_form })
