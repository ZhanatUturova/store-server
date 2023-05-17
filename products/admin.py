from django.contrib import admin
from .models import *


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductForm(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    # readonly_fields = ('description', )
    search_fields = ('name',)
    ordering = ('name', '-price')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0
