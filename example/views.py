from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here
#def homeview(request)
#    return HttpResponse('hellow world')
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'