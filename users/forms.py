from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Abebe'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Feyisa'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'abebefeyisa@gmail.com'}))
    phone = forms.CharField(required=True, max_length=13, widget=forms.TextInput(attrs={'placeholder': '+251911807090'}))
    profile = forms.ImageField(help_text="Upload your profile picture", required=False)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'region', 'sex', 'phone', 'user_type', 'profile')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        mode = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomLoginForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': 'login__field', 
         'palceholder': ''}
        )
        self.fields['password'].widget.attrs.update(
        {'class': 'login__field'}
        )
