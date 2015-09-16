from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', views.BetaSignupForm, name='beta'),
)
