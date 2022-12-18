from django.urls import path, include

from farmers_market.miscellaneous.views import IndexView, AllGroceryListView, basic_grocery_details, \
    AllCompanyListView, about_us_page

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', about_us_page, name='about us'),
    path('dashboard/', include([
        path('', AllGroceryListView.as_view(), name='grocery list'),
        path('basic_grocery_view/<slug:grocery_slug>/', basic_grocery_details, name='basic details view'),
        #path('review/<str:grocery_id>/', review_grocery, name='review grocery'),
        path('companies/', AllCompanyListView.as_view(), name='company list'),
    ])),
]
