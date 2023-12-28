# myapp/urls.py
from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('home_organizer/', views.home_organizer, name='home_organizer'),
    path('register_organizer/', views.register_organizer, name='register_organizer'),
    path('organizer_registration_pending/', views.organizer_registration_pending, name='organizer_registration_pending'),
    path('login_organizer/', views.login_organizer, name='login_organizer'),
    path('logout_organizer/', views.logout_organizer, name='logout_organizer'),
    path('view_event_organizer/', views.view_event_organizer, name='view_event_organizer'),
    path('create_event_organizer/', views.create_event_organizer, name='create_event_organizer'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),

]
