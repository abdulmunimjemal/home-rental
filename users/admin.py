from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    readonly_fields = ('joined_at',)
    
    list_display = ['first_name', 'last_name', 'email', 'sex', 'joined_at', 'region', 'user_type', 'phone', 'profile']
    list_filter = ('is_superuser', 'sex', 'user_type', 'region',)
    fieldsets =  UserAdmin.fieldsets + (
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,
         {'fields': ('first_name', 'email', 'last_name', 'phone', 'sex', 'region', 'user_type')}),
    )
    search_fields = ('email', 'sex', 'region', 'user_type', 'first_name', 'last_name',)
    ordering = ('email', 'user_type', 'sex', 'region')
    

admin.site.register(CustomUser, CustomUserAdmin)

