"""identicons URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include(('users.urls', 'users'), namespace='users')),
    path('generator', include(('generator.urls', 'generator'), namespace='generator')),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
