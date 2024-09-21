from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index Page
def index(request):
    return HttpResponse("Hello. world. You're at the users index")

def signup(request):
    return HttpResponse("Test")

def login(request):
    return render(request, "users/login.html")

def profile(request, user_id):
    return HttpResponse("test")

def edit_profile(request):
    return HttpResonse("edit profile")
