from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Buket
from django.contrib.auth.decorators import login_required


def buy(request):
    return render(request, 'buy.html')

def share(request):
    return render(request, 'share.html')

@login_required
def buket(request):
    if request.method == 'POST':
        busketName = request.POST.get('busketName')
        busketPrice = request.POST.get('busketPrice')
        busketShop = request.POST.get('busketShop')
        busketShopUrl = request.POST.get('busketShopUrl')
        busketCategory = request.POST.get('busketCategory')

        buket = Buket(
            user=request.user,
            busketName=busketName,
            busketPrice=busketPrice,
            busketShop=busketShop,
            busketShopUrl=busketShopUrl,
            busketCategory=busketCategory
        )
        buket.save()
         
    bukets = Buket.objects.filter(user=request.user) 
    return render(request, 'bucket.html', {'bukets': bukets})



@login_required
def buket_detail(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    return render(request, 'buket_detail.html', {'buket': buket})

@login_required
def buket_delete(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    if request.method == 'POST':
        buket.delete()
        return redirect('buket_list')
    return render(request, 'buket_confirm_delete.html', {'buket': buket})
