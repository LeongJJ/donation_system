# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Organizer, FundraisingEvent
from .forms import OrganizerRegistrationForm, FundraisingEventForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout



def home_organizer(request):
    latest_events = FundraisingEvent.objects.order_by('-created_date')[:3]
    return render(request,'organizer/home_organizer.html', {'latest_events': latest_events})

#register
def register_organizer(request):
    if request.method == 'POST':
        form = OrganizerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print("Data Saved!")
            organizer = form.save(commit=False)
            organizer.save()
            return redirect('organizer:organizer_registration_pending')  # You can customize this URL
        else:
            print(form.errors)
    else:
        form = OrganizerRegistrationForm()

    return render(request, 'organizer/register.html', {'form': form})

def organizer_registration_pending(request):
    return render(request, 'organizer/registration_pending.html')

def login_organizer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate_organizer(username, password)
        if user.is_approved:
            auth_login(request, user)
            print("Login Successful!")
            return redirect('organizer:home_organizer')  # You can customize this URL for the organizer's dashboard
        elif user is not None and not user.is_approved:
             messages.error(request, 'Your account is still pending approval.')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'organizer/login.html')

#organizer authentication function
def authenticate_organizer(username, password):
    try:
        organizer = Organizer.objects.get(username=username)

        if check_password(password, organizer.password):
            if organizer.is_approved:
                return organizer
            else:
                print("Authentication failed: Account not approved.")
                return None
        else:
            print("Authentication failed: Incorrect password.")
            return None
    except Organizer.DoesNotExist:
        print("Authentication failed: Organizer not found.")
        return None

def logout_organizer(request):
    logout(request)
    return redirect('home')



def event_detail(request, event_id):
    event = get_object_or_404(FundraisingEvent, pk=event_id)
    return render(request, 'fundraising/event_detail.html', {'event': event})


def create_event_organizer(request):
    if request.method == 'POST':
        form = FundraisingEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer:home_organizer')
    else:
        form = FundraisingEventForm()
    return render(request,'organizer/create_event_organizer.html', {'form': form})


def view_event_organizer(request):
    all_events = FundraisingEvent.objects.order_by('-created_date')
    return render(request,'organizer/view_event_organizer.html', {'all_events': all_events})
