from django.contrib.auth import models as auth_model
from django.core import validators
from django.db import models


class AppUser(auth_model.AbstractUser):
    MAX_LEN_USERNAME = 30
    MAX_LEN_EMAIL = 50
    MAX_LEN_PASSWORD = 50
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    MIN_LEN_PASSWORD = 8
    MIN_LEN_USERNAME = 5

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
        ),
        unique=True,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        unique=True,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
    )
    # password = models.CharField(
    #     max_length=MAX_LEN_PASSWORD,
    #     validators=(
    #         validators.MinLengthValidator(MIN_LEN_PASSWORD),
    #     ),
    #     null=False,
    #     blank=False,
    #)

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

