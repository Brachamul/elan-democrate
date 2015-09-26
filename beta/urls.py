from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', views.BetaSignupForm, name='beta'),
	url(r'^list$', views.beta_candidate_list, name='beta_candidate_list'),
	url(r'^activate/(?P<pk>[0-9]+)$', views.activate_beta_candidate, name='activate_beta_candidate'),
	url(r'^(?P<email>[\x00-\x7F]+)$', views.BetaSignupForm, name="beta_with_email"),
)
