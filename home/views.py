from django.shortcuts import render

def home(request):
    return render(request, 'home_test.html')


# Create your views here.
