from django.urls import path, include

from farmers_market.groceries.views import add_grocery, details_grocery, edit_grocery, delete_grocery, GroceryListView

urlpatterns = (
    path('add/', add_grocery, name='add grocery'),
    path('mygroceries/', GroceryListView.as_view(), name='mygroceries'),
    path('<str:username>/grocery/<slug:grocery_slug>/', include([
        path('', details_grocery, name='details grocery'),
        path('edit/', edit_grocery, name='edit grocery'),
        path('delete/', delete_grocery, name='delete grocery'),
    ]))
)
