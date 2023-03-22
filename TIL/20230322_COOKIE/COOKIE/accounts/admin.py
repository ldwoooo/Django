from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# UserAdmin: User 데이터를 입력받는 Form
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "nickname", )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "nickname",),
            },
        ),
    )
admin.site.register(User, CustomUserAdmin)