from django.contrib import admin
from .models import User  # Sesuaikan dengan path ke model User Anda

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'groups', 'user_permissions')

admin.site.register(User, UserAdmin)
