from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

# Register your models here.
@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    #pass
    #fieldsets = [] # 이렇게만 해도 models에서 추가한 정보가 표시됨.

    fieldsets = [
        (("개인정보", {"fields": ["email", "password"]})),
        (("개인정보", {"fields": ["profile_image", "username"]})),
        ]