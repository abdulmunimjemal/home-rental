from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms

REGIONS = [
        ('AA', 'አዲስ አበባ'),
        ('DDW', 'ድሬደዋ'),
        ('OR', 'ኦሮሚያ'),
        ('AM', 'አምራ'),
        ('TG', 'ትግራይ'),
        ('AF', 'አፋር'),
        ('HR', 'ሀረሪ'),
        ('SD', 'ሲዳማ'),
        ('SNNPE', 'ደቡብ ክልል'),
        ('GM', 'ጋምቤላ'),
        ('BG', 'ቤኒሻንጉል ጉሙዝ'),
    ]
TYPE = [
        ('buyer', 'ቤት ፈላጊ'),
        ('seller', 'ደላላ'),
    ]
SEX = [
        ('M', 'ወንድ'),
        ('F', 'ሴት'),
    ]

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Abebe'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Feyisa'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'abebefeyisa@gmail.com'}))
    phone = forms.CharField(required=True, max_length=13, widget=forms.TextInput(attrs={'placeholder': '+251911807090'}))
    profile = forms.ImageField(help_text="Upload your profile picture", required=False)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'region', 'sex', 'phone', 'user_type', 'profile')

class RegisterForm(UserCreationForm):
        email = forms.EmailField(
        max_length=100,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email',  'autocomplete': 'off'}),
        label=''
        )
        first_name = forms.CharField(
        max_length=100,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
        label=''
        )
        last_name = forms.CharField(
        max_length=100,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg'}),
        label=''
        )
        phone = forms.CharField(required=True, max_length=13, widget=forms.TextInput(attrs={'class': 'form-control'}), label='')
        sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect(attrs={'class': 'form-check-input'})) # class="" 

        region = forms.ChoiceField(choices=REGIONS, 
                                widget=forms.Select(attrs={'class': 'select form-control-lg',}),
                                ) # class="" 
        user_type = forms.ChoiceField(choices=TYPE, 
                                widget=forms.Select(attrs={'class': 'select form-control-lg' }),
                                label='') # class="" 
        password1 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password', 'autocomplete': 'off'}),
        label=''
        )
        password2 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password Again', 'autocomplete': 'off'}),
        label=''
        )
        class Meta(UserCreationForm):
            model = CustomUser
            fields = ('first_name', 'last_name', 'email', 'phone', 'region', 'sex', 'user_type', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        mode = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomLoginForm(AuthenticationForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': 'form-control form-control-lg', 
         'palceholder': 'Enter Your Email'}
        )
        self.fields['password'].widget.attrs.update(
        {'class': 'form-control form-control-lg',
         'placehodler': 'password'
         }
        
        )
