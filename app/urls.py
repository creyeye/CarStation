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
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('login/', views.user_login, name='user_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('post_create/', views.post_create, name='post_create'),
    path('logout/', views.user_logout, name='logout'),
]
