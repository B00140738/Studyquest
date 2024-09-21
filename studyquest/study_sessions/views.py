from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index Page
def index(request):
    return HttpResponse("Hello, world. You're at the Study Sessions index")
