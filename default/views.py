from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organizer.models import FundraisingEvent

def home(request):
    latest_events = FundraisingEvent.objects.order_by('-created_date')[:3]
    return render(request,'default/homepage.html', {'latest_events': latest_events})

def about_us(request):
    return render(request,'default/about_us.html')

def view_event(request):
   return render(request,'default/view_event.html')





