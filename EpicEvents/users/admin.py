from django.contrib import admin

# Register your models here.
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    if not User.team == "MANAGEMENT":
        # site aadmin interdit
        pass
