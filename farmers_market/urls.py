from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmers_market.miscellaneous.urls')),
    path('accounts/', include('farmers_market.accounts.urls')),
    path('companies/', include('farmers_market.companies.urls')),
    path('groceries/', include('farmers_market.groceries.urls')),
    path('news/', include('farmers_market.news.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
