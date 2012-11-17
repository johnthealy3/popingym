from django.shortcuts import render
from django.http import HttpResponseRedirect
from gymfinder.models import *
from gymfinder.helpers import get_lat_lng

def login(request):
    return render(request, 'login.html', {} )

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
