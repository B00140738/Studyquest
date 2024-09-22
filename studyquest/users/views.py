from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Hello. world. You're at the users index")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.create_user(username=username, name=name, email=email, password=password)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard', user)
        except ValueError as e:
            messages.error(request, str(e))
    
    return render(request, "users/signup.html")

# Login Logic

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "users/login.html")

# Dashboard

@login_required
def dashboard(request):
    user = request.user  # Get the logged-in user
    return render(request, "users/dashboard.html", {"user": user})  # Pass the entire user object

def profile(request, user_id):
    return HttpResponse("test")

def edit_profile(request):
    return HttpResonse("edit profile")
