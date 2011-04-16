from django.views.generic import simple


def home(request):
    return simple.direct_to_template(request, template='home/home.html')
