from django.conf.urls.defaults import patterns, include, url

from profiles.views import ProfileView

urlpatterns = patterns('',
    url(r'^$', ProfileView.as_view(), name='profiles_list'),
    url(r'^login/$', 'profiles.views.login', name='profiles_login'),
)

