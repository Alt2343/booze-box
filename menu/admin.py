from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    list_filter = ['parent']
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'brand', 'alcohol_type', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('alcohol_type', 'available', 'category', 'created', 'updated')
    search_fields = ('name', 'brand', 'description')
    prepopulated_fields = {'slug': ('name', 'brand')}
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'alcohol_type', 'image')
        }),
        ('Детали', {
            'fields': ('brand', 'country', 'volume', 'strength', 'description')
        }),
        ('Цена и наличие', {
            'fields': ('price', 'stock', 'available')
        }),
        ('Даты', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )