from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Include the core app's URLs
    path('__reload__/', include('django_browser_reload.urls')),  # For live reloading during development
]
