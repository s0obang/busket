from django import forms
from .models import Profile

class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_userImage_form.html'
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['nickname','userImage']
        widgets = {
            'userImage': CustomClearableFileInput(),  # 커스텀 위젯 사용
        }
        
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("이미 사용 중인 닉네임입니다.")
        return nickname

    