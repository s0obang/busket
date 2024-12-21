from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Buket
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



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


def buket_count(request):
    bukets = Buket.objects.filter(user=request.user)
    countP =0 
    count=0
    for b in bukets:
        countP += int(b.busketPrice)
        count+=1

    counts = {
        "countP": countP,
        "count": count,
    }
    return counts

def busket_category(request):
    bukets_b = Buket.objects.filter(user=request.user, isBuy=True)
    if(bukets_b.count()==0):
        max_buy_str = "-"
        min_buy_str = "-"
    else:
        clothes_b = bukets_b.filter(busketCategory="의류").count()
        interior_b = bukets_b.filter(busketCategory="인테리어").count()
        goods_b = bukets_b.filter(busketCategory="굿즈").count()
        food_b = bukets_b.filter(busketCategory="음식").count()
        hobby_b = bukets_b.filter(busketCategory="취미").count()
        etc_b = bukets_b.filter(busketCategory="기타").count()

        max_buy = max(clothes_b, interior_b, goods_b, food_b, hobby_b, etc_b)
        min_buy = min(clothes_b, interior_b, goods_b, food_b, hobby_b, etc_b)

        if max_buy == clothes_b:
            max_buy_str = "의류"
        elif max_buy == interior_b:
            max_buy_str = "인테리어"
        elif max_buy == goods_b:
            max_buy_str = "굿즈"
        elif max_buy == food_b:
            max_buy_str = "음식"
        elif max_buy == hobby_b:
            max_buy_str = "취미"
        else:
            max_buy_str = "기타"

        if min_buy == clothes_b:
            min_buy_str = "의류"
        elif min_buy == interior_b:
            min_buy_str = "인테리어"
        elif min_buy == goods_b:
            min_buy_str = "굿즈"
        elif min_buy == food_b:
            min_buy_str = "음식"
        elif min_buy == hobby_b:
            min_buy_str = "취미"
        else:
            min_buy_str = "기타"

    bukets_nb = Buket.objects.filter(user=request.user)
    if(bukets_nb.count()==0):
        max_nbuy_str = "-"
        min_nbuy_str = "-"
    else:  
        clothes_nb = bukets_nb.filter(busketCategory="의류").count()
        interior_nb = bukets_nb.filter(busketCategory="인테리어").count()
        goods_nb = bukets_nb.filter(busketCategory="굿즈").count()
        food_nb = bukets_nb.filter(busketCategory="음식").count()
        hobby_nb = bukets_nb.filter(busketCategory="취미").count()
        etc_nb = bukets_nb.filter(busketCategory="기타").count()

        max_nbuy = max(clothes_nb, interior_nb, goods_nb, food_nb, hobby_nb, etc_nb)
        min_nbuy = min(clothes_nb, interior_nb, goods_nb, food_nb, hobby_nb, etc_nb)

        if max_nbuy == clothes_nb:
            max_nbuy_str = "의류"
        elif max_nbuy == interior_nb:
            max_nbuy_str = "인테리어"
        elif max_nbuy == goods_nb:
            max_nbuy_str = "굿즈"
        elif max_nbuy == food_nb:
            max_nbuy_str = "음식"
        elif max_nbuy == hobby_nb:
            max_nbuy_str = "취미"
        else:
            max_nbuy_str = "기타"

        if min_nbuy == clothes_nb:
            min_nbuy_str = "의류"
        elif min_nbuy == interior_nb:
            min_nbuy_str = "인테리어"
        elif min_nbuy == goods_nb:
            min_nbuy_str = "굿즈"
        elif min_nbuy == food_nb:
            min_nbuy_str = "음식"
        elif min_nbuy == hobby_nb:
            min_nbuy_str = "취미"
        else:
            min_nbuy_str = "기타"

    report = {
        "max_buy": max_buy_str,
        "min_buy": min_buy_str,
        "max_nbuy": max_nbuy_str,
        "min_nbuy": min_nbuy_str,
    }

    return report


def buket_detail(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    return render(request, 'buket_detail.html', {'buket': buket})


def buket_delete(request, pk):
    buket = get_object_or_404(Buket, pk=pk, user=request.user)
    if request.method == 'POST':
        buket.delete()
        return redirect('buket_list')
    return render(request, 'buket_confirm_delete.html', {'buket': buket})
