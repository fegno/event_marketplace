from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.user.models import User


# Register your models here.

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'username')
#
#     list_filter = ('is_superuser', 'is_staff')
#
#     fieldsets = (
#         # (None, {
#         #     'fields': ('first_name', 'last_name', 'email', 'username')
#         # }),
#         ('Personal Info', {
#             'fields': ('first_name', 'last_name')
#         }),
#     )


admin.site.register(User, UserAdmin)
