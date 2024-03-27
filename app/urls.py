from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('404/', views.index),
    path('about/', views.index, name='about'),
    path('booking/', views.index, name='booking'),
    path('contact/', views.index),
    path('index/', views.index, name='index'),
    path('service/', views.index),
    path('team/', views.index),
    path('testimonial/', views.index),
]
