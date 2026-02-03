from django.contrib import admin
from .models import UserProfile

# Register UserProfile so you can edit roles in admin
admin.site.register(UserProfile)
