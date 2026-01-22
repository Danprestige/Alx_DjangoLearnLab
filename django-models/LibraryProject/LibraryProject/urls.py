from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # include relationship_app routes at root
    path('', include('relationship_app.urls')),
]

