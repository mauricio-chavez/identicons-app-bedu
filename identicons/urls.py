"""identicons URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path('generator', include(('generator.urls', 'generator'), namespace='generator')),
]
