from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Admin configuration for UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'age', 'country', 'city', 'company', 'position')
    # Fields to enable search functionality in the admin
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name', 'age', 'country', 'city', 'company', 'position')
    # Fields that can be used to sort the list view
    sortable_by = ('user', 'age', 'country', 'city', 'company', 'position')

admin.site.register(UserProfile, UserProfileAdmin)
