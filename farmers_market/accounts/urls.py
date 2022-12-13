from django.urls import path, include

from farmers_market.accounts.views import RegisterView, LoginView, LogoutView, UserDetailsView, UserEditView, \
    UserDeleteView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register profile'),
    path('login/', LoginView.as_view(), name='login profile'),
    path('logout/', LogoutView.as_view(), name='logout profile'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details profile'),
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', UserDeleteView.as_view(), name='delete profile'),
    ]))
)