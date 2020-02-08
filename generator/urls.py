"""Generator app URLs"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.identicon, name='identicon'),
]
