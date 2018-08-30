from django.urls import path
from example.views import PublisherList
from example import views

urlpatterns = [
    path('publishers/', PublisherList.as_view()),
    path('display_meta/', views.ua_display_good1, name='displaymeta'),
    path('search_form/', views.search_form, name ='search'),
    path('search/', views.search),
 #   path('contact/thanks/', views.thanks),
    path('contact/', views.contact),
]
