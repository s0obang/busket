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

    