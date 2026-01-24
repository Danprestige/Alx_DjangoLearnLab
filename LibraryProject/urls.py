from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),               # FIX 1 (Admin)
    path('', include('relationship_app.urls')),    # App routes
    path('accounts/', include('django.contrib.auth.urls')),  # FIX 2 (Auth)
]
