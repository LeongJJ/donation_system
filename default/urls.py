from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'default'),
    path('home/', views.home, name= 'home'),
    path('about_us/', views.about_us, name='about_us'),
    path('view_event/', views.view_event, name='view_event'),
]