from .models import Category, News
from modeltranslation.translator import register, TranslationOptions


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('name', 'text', 'dateCreation', 'author', 'category', )


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name', )
