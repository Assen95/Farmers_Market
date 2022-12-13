from django.contrib import admin

from farmers_market.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication', 'author')
    search_fields = ('title__startswith',)