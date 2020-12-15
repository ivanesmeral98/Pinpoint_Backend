from django.contrib import admin

# Register your models here.
from .models import UserProfile, CollaborativeMap, Map, Notification, Pin, Request, Review, Tag

admin.site.register(UserProfile)
admin.site.register(CollaborativeMap)
admin.site.register(Map)
admin.site.register(Notification)
admin.site.register(Pin)
admin.site.register(Request)
admin.site.register(Review)
admin.site.register(Tag)