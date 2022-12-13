from django.contrib import admin

from farmers_market.miscellaneous.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'customer_rating', 'user',)
