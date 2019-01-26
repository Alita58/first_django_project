from django.contrib import admin

# Register your models here.
from .models import (
    Posts, Activity, Countries, Destination, Text, CitizenshipCountries
)

admin.site.register(Posts)
admin.site.register(Activity)
admin.site.register(Countries)
admin.site.register(Destination)
admin.site.register(Text)
admin.site.register(CitizenshipCountries)
