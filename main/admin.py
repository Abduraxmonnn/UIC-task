from django.contrib import admin

from main.models import Product, Category, Tag, TagsCategory


# Register your models here.

@admin.register(TagsCategory)
class TagsCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
