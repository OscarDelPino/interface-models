from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'country', 'city', 'company', 'position')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'age', 'country', 'city', 'company', 'position')
    sortable_by = ('user', 'age', 'country', 'city', 'company', 'position')

admin.site.register(UserProfile, UserProfileAdmin)
