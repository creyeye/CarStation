from django.urls import path
from . import views


urlpatterns = [
    path('404/', views.error, name='error'),
    path('about/', views.index, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('post_list/', views.PostListViews.as_view(), name='post_list'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('login/', views.user_login, name='user_login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('post_create/', views.post_create, name='post_create'),
    path('logout/', views.user_logout, name='logout'),
    path('post_update/<int:pk>/', views.PostUpdate.as_view(), name='post_update'),
]
