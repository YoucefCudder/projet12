from django.conf import settings
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin


# @admin.register(User, UserAdmin)
# class UserAdmin(admin.ModelAdmin):
#     if not User.team == "MANAGEMENT":
#         # site aadmin interdit
#         pass
from django.contrib.auth.models import User

#
# admin.site.register( )
