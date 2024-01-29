from django.contrib import admin
from .models import News, Author, Category
from modeltranslation.admin import TranslationAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category')
    list_filter = ('name', 'author', 'category')
    search_fields = ('name', 'category')


class CategoryAdmin(TranslationAdmin):
    model = Category


class NewsAdmin(TranslationAdmin):
    model = News


admin.site.register(News, ProductAdmin)
admin.site.register(Author)
admin.site.register(Category)

