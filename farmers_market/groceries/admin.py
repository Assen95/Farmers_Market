from django.contrib import admin

from farmers_market.groceries.models import Grocery, Category


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quality_rating', 'slug', 'date_created', 'expiry_date', 'user', 'company')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
