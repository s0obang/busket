from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

# from .forms import 

#password1:비밀번호, password2:비밀번호확인, username:ID

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            auth.login(request, user)
            return redirect('home:home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return redirect('home:home')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home:home')


def notloginmy(request):
    return render(request, 'my.html')

def my(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile=get_object_or_404(Profile, user=user)
    
    if request.method == 'GET':
        profile_update_form = ProfileForm(instance=profile)
    else:
        profile_update_form=ProfileForm(request.POST,request.FILES, instance=profile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('accounts:my',user_id)     
        # else:
            # return redirect('accounts:my',user_id)
            # 유효하지 않은 경우 동작 (에러를 표시하거나 다시 렌더링)
    context = {
        'profile':profile,
        'profile_update_form':profile_update_form,
        'user_id':user_id
        }
    return render(request,'my.html',context)