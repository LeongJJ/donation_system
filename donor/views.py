from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, EditProfileForm


def home(request):
    return render(request,'default/homepage.html')

def view_event(request):
   return render(request,'default/view_event.html')


#register function
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('donor:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'donor/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Username: {username}, Password: {password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User authenticated successfully")
                return redirect('home')  # Change 'home' to your desired home page URL
            else:
                print("Authentication failed")
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'donor/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'donor/view_profile.html', {'user': user})

@login_required
def edit_profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'donor/view_profile.html', {'form': form})