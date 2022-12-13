from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from farmers_market.companies.validators import validate_image

'''
name, logo, location, description, user
'''

UserModel = get_user_model()


class Company(models.Model):
    MAX_NAME_LEN = 30
    MAX_LOCATION_LEN = 30
    MAX_DESCRIPTION_LEN = 255

    MIN_NAME_LEN = 4
    MIN_DESCRIPTION_LEN = 10

    name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=[
            validators.MinLengthValidator(MIN_NAME_LEN),
        ],
        null=False,
        blank=False,
    )

    logo = models.ImageField(
        upload_to='mediafiles',
        validators=(
            validate_image,
        ),
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=[
            validators.MinLengthValidator(MIN_DESCRIPTION_LEN),
        ],
        blank=True,
        null=True,
    )

    date_formed = models.DateField()

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

