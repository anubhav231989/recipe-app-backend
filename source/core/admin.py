from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Information"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Dates"), {"fields": ("last_login",)})
    )
    #READ MORE ON THIS.
    add_fieldsets = (
        ("None", {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2",)
        }),
    )

admin.site.register(User, UserAdmin)

