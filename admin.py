from django.contrib import admin
from .models import Message, Like, Rating

admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Rating)
