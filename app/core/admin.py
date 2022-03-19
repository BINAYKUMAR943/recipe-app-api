from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

"""For converting string in our python to human readable text"""
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering=['id']
    list_display=['email','name']
    """Reason for adding fieldsets"""
    fieldsets=(
    (None,{'fields':('email','password',)}),
    # (_('Personal_info'),{'fields':('name',)}),
    (_('Permissions'),{'fields':('is_active','is_staff','is_superuser',)}),
    (_('Important dates'),{'fields':('last_login',)})
    )

    add_fieldsets=(
    # Addded the class of the field taken from the django dcoumentation
    (None, {'classes':('wide',),'fields':('email','password1','password2')}),

    )

admin.site.register(models.User,UserAdmin)
