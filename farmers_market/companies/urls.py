from django.urls import path, include

from farmers_market.companies.views import add_company, view_company, edit_company, delete_company

urlpatterns = (
    path('add/', add_company, name='add company'),
    path('<int:pk>/', include([
        path('', view_company, name='details company'),
        path('edit/', edit_company, name='edit company'),
        path('delete/', delete_company, name='delete company'),
    ])),
)