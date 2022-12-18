from django.urls import path, include

from farmers_market.news.views import add_news, view_news, edit_news, delete_news, AllNewsListView

urlpatterns = (
    path('add/', add_news, name='add news'),
    path('all-news', AllNewsListView.as_view(), name='news list'),
    path('<int:news_id>/details/', view_news, name='details news'),
    path('<int:author_id>/news/<int:news_id>/', include([
        path('edit/', edit_news, name='edit news'),
        path('delete/', delete_news, name='delete news')
    ]))
)