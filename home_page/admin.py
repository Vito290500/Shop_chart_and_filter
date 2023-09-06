from django.contrib import admin

# Register your models here.
from .models import ShopItem, Category, Brand

admin.site.register(ShopItem)
admin.site.register(Category)
admin.site.register(Brand)