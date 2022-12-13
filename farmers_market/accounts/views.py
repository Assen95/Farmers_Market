from django.contrib.auth.models import Group
from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, get_user_model

from farmers_market.accounts.forms import UserCreationForm
from farmers_market.companies.models import Company

UserModel = get_user_model()


# Signs Up a User
class RegisterView(views.CreateView):
    template_name = 'profile/create-profile.html'
    form_class = UserCreationForm

    def get_success_url(self):
        group = Group.objects.get(name='User')
        group.user_set.add(self.object)
        return reverse_lazy('index')


# Login an existing User
class LoginView(auth_views.LoginView):
    template_name = 'profile/login-profile.html'


# Logouts current session
class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


# Shows current user's details
class UserDetailsView(views.DetailView):
    template_name = 'profile/details-profile.html'
    context_object_name = 'profile'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user = self.object
        return context


# Edits user's existing information
class UserEditView(views.UpdateView):
    template_name = 'profile/edit-profile.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'profile_picture')

    # This makes it take the unique details for the id'd user
    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })


# Deletes user
class UserDeleteView(views.DeleteView):
    template_name = 'profile/delete-profile.html'
    model = UserModel
    success_url = reverse_lazy('index')
