from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Buket
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def buy(request):
    return render(request, 'buy.html')

def share(request):
    return render(request, 'share.html')


def buket(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            busketName = request.POST.get('busketName')
            busketPrice = request.POST.get('busketPrice')
            busketShop = request.POST.get('busketShop')
            busketShopUrl = request.POST.get('busketShopUrl')
            busket = request.POST.get('busket')
            Image = '비스켓 2.svg'
            if(busket=="2"):
                Image='비스켓 2.svg'
            elif(busket=="4"):
                Image='비스켓 4.svg'
            elif(busket=="8"):
                Image='비스켓 8.svg'
            elif(busket=="9"):
                Image='비스켓 9.svg'  
            busketCategory = request.POST.get('busketCategory')

            buket = Buket(
                user=request.user,
                busketName=busketName,
                busketPrice=busketPrice,
                busketShop=busketShop,
                busketShopUrl=busketShopUrl,
                busketCategory=busketCategory,
                Image=Image
            )
            buket.save()

        bukets = Buket.objects.filter(user=request.user).filter(isBuy=False) 

        #이 아래가 categorie별로 리턴하는거야
        categories = {
            "clothes": bukets.filter(busketCategory="의류"),
            "interior": bukets.filter(busketCategory="인테리어"),
            "goods": bukets.filter(busketCategory="굿즈"),
            "food": bukets.filter(busketCategory="음식"),
            "hobby": bukets.filter(busketCategory="취미"),
            "etc": bukets.filter(busketCategory="기타"),
        }
        return render(request, 'bucket.html', {'bukets': bukets, 'categories': categories})
    else:
        return render(request, 'bucket.html')

def buy(request):
    if request.user.is_authenticated:

        bukets = Buket.objects.filter(user=request.user).filter(isBuy=False)
        buketsBuy = Buket.objects.filter(user=request.user).filter(isBuy=True)  
        if request.method == 'POST':
            data = json.loads(request.body)
            selected_ids = data.get('selectedIds', [])
            bukets_to_update = Buket.objects.filter(id__in=selected_ids, user=request.user)
            bukets_to_update.update(isBuy=True)

            return render(request, 'buy.html', {'bukets': bukets, 'buketsBuy':buketsBuy})

        return render(request, 'buy.html', {'bukets': bukets, 'buketsBuy':buketsBuy})
    else:
        return render(request, 'buy.html')






def buket_detail(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    return render(request, 'buket_detail.html', {'buket': buket})


def buket_delete(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    if request.method == 'POST':
        buket.delete()
        return redirect('buket_list')
    return render(request, 'buket_confirm_delete.html', {'buket': buket})
