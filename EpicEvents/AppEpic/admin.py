from django.contrib import admin

# Register your modls here.

from .models import Client, Contract, Event

admin.site.register([Client, Contract, Event])

