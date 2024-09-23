from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def my(request):
    return render(request, 'my.html')

# Create your views here.
