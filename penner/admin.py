from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'buyer', 'amount', 'purchased', ]
    list_filter = ['created', 'purchased', 'buyer']
    search_fields = ['name', 'notes']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['buyer']
    date_hierarchy = 'purchased'
    ordering = ['purchased', 'name']