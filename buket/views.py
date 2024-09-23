from django.shortcuts import render

def buket(request):
    return render(request, 'bucket.html')

def buy(request):
    return render(request, 'buy.html')

def share(request):
    return render(request, 'share.html')

# Create your views here.
