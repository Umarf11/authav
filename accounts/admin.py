from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("id", "email", "name", "tc", "is_admin")
    list_filter = ("is_admin",)  # Fixed: Ensure it's a tuple

    # Corrected fieldsets with the proper 'fields' key
    fieldsets = (
        (None, {"fields": ("email", "password")}),  # Fixed key
        ("Personal info", {"fields": ("name", "tc")}),
        ("Permissions", {"fields": ("is_admin",)}),  # Fixed: Fields must be a tuple
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),  # Fixed: Ensure classes is a tuple
                "fields": ("email", "name", "tc", "password1", "password2"),
            },
        ),
    )

    search_fields = ("email",)  # Fixed: Ensure it's a tuple
    ordering = ("email", "id")
    filter_horizontal = ()

# Register the User model with the custom admin


admin.site.register(User, UserModelAdmin)
