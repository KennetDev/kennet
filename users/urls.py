from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('users/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),
]