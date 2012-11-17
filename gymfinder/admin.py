from django.contrib import admin
from gymfinder import models
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class GymAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},    
      }

#admin.site.register(models.Gym, GymAdmin)
