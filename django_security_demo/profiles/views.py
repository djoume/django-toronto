from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from profiles.models import UserProfile


class ProfileView(ListView):
    model = UserProfile
    template_name = 'profiles/list.html'


def login(request):
    response = HttpResponseRedirect('/')
    response['Location'] = request.GET.get('next', reverse('profiles_list'))
    response.set_cookie('next', request.GET['next'])
    return response
