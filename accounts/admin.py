from django.contrib import admin
from .models import CustomUser, BlockList

admin.site.register(BlockList)
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone']
    list_filter = ['username', 'phone']
    search_fields = ['username', 'phone']
    
