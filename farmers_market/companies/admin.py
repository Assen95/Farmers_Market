from django.contrib import admin

from farmers_market.companies.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date_formed',)
    list_filter = ('name',)
    search_fields = ('name__startswith',)