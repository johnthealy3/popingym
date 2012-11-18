from django.db import models
from django_google_maps import fields as map_fields
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.contrib.auth.models import User
import json

class Location(models.Model):
    address = models.CharField(max_length=255, blank=True)
    latlng   = models.CharField(blank=True, max_length=100, help_text=(u'Note: This field will be filled-in automatically based on the other address bits.'))

    def __unicode__(self):
        return self.latlng

class Message(models.Model):
    user = models.ForeignKey(User)
    message_id = models.CharField(max_length=255)
    message = models.CharField(max_length=8000)

class Gym(models.Model):
    #address = map_fields.AddressField(max_length=200)
    #geolocation = map_fields.GeoLocationField(max_length=100)
  
    name    = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city     = models.CharField(max_length=255, blank=True)
    state    = models.CharField(max_length=2, blank=True)
    zip      = models.CharField(max_length=10, blank=True)
    country  = models.CharField(blank=True, max_length=100)
    latlng   = models.CharField(blank=True, max_length=100, help_text=(u'Note: This field will be filled-in automatically based on the other address bits.'))
    phone    = models.CharField(max_length=20, blank=True)
    email    = models.EmailField(blank=True)
    website  = models.URLField(blank=True)
    about    = models.TextField(blank=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        # If latlng has no value:
        if not self.latlng:
            # Add + between fields with values:
            location = '+'.join(filter(None, (self.address1, self.address2, self.city, self.state, self.zip, self.country)))
            # Attempt to get latitude/longitude from Google Geocoder service v.3:
            self.latlng = get_lat_lng(location)
        super(Gym, self).save(*args, **kwargs)
    
class LocationForm(forms.Form):    
    address = forms.CharField(
        label = "What is your address?",
        max_length = 200,
        required = True,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Enter location:',
                'address',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        super(LocationForm, self).__init__(*args, **kwargs)

    
