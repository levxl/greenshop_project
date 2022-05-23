from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Flowers)
admin.site.register(RatingStar)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("star", "flowers", "ip")

