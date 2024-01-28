from django.contrib import admin
from .models import News, Author, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'category')
    list_filter = ('name', 'author', 'category')
    search_fields = ('name', 'category')


admin.site.register(News, ProductAdmin)
admin.site.register(Author)
admin.site.register(Category)

