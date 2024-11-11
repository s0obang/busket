from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
# from .forms import 

#password1:비밀번호, password2:비밀번호확인, username:ID

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            auth.login(request, user)
            return redirect('home:home')
        return render(request, 'signup_test.html')
    return render(request, 'signup_test.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home:home')
        else:
            return render(request, 'login_test.html')
    else:
        return render(request, 'login_test.html')

def logout(request):
    auth.logout(request)
    return redirect('home:home')

def my(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile=get_object_or_404(Profile, user=user)
    return render(request, 'my_test.html', {'profile':profile})

#my_update : 프로필 수정 함수
#profile_update_form : 프로필 수정 폼
def my_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile=get_object_or_404(Profile, user=user)
    if request.method == 'GET':
        profile_update_form = ProfileForm(instance=profile)
    else:
        profile_update_form=ProfileForm(request.POST,request.FILES, instance=profile)
        if profile_update_form.is_valid():
            #기본프로필로 체크박스 클릭 시 default.jpeg로 프로필 바뀜
            if 'userImage-clear' in request.POST: 
                profile.userImage = 'default.jpeg'
            profile_update_form.save()
            return redirect('accounts:my',user_id)     
    context = {
        'profile_update_form':profile_update_form,
        'user_id':user_id
        }
    return render(request,'my_update_test.html',context)
    # Create your views here.
