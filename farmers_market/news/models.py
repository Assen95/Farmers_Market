from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from farmers_market.companies.validators import validate_image

'''title, description, image(optional), publication, author(user)'''
UserModel = get_user_model()


class News(models.Model):
    MAX_TITLE_LEN = 50
    MAX_DESCRIPTION_LEN = 255

    MIN_DESCRIPTION_LEN = 10
    MIN_TITLE_LEN = 5

    title = models.CharField(
        max_length=MAX_TITLE_LEN,
        validators=[
            validators.MinLengthValidator(MIN_TITLE_LEN),
        ],
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LEN),
        ),
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='news',
        validators=(
            validate_image,
        ),
        null=True,
        blank=True,
    )

    publication = models.DateTimeField(
        auto_now=True,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
