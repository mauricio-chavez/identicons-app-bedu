"""Users app URLs"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signoff', views.signoff, name='signoff'),
    path('signup', views.signup, name='signup')
]
