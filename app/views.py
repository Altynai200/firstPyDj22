from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def appIndex(request):
    appList = models.App.objects.all()
    return render(request, 'app/index.html', {'appList': appList})


class AppIndex(ListView):
    model = models.App
    template_name = 'app/index.html'


# class AppShow(View):
def AppShow(request, slug):
    app = models.App.objects.get(url=slug)
    return render(request, 'app/show.html', {"app": app})


# def handler404(request, exception):
#     return render(request, '404page.html', status=404)
#
#
# def handler500(exception):
#     return render(template_name='404page.html', status=500)

# class AppShow(DetailView):
#     model = models.App
#     slug_field = "url"
#     template_name = "app/show.html"
