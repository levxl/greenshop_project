from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name')


@register(Flowers)
class ActorTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

