from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


# Register
class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {'username': auth_forms.UsernameField}


# Edit
class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'profile_picture',)
        field_classes = {'username': auth_forms.UsernameField}