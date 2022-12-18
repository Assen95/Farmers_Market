from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from farmers_market.companies.models import Company
from farmers_market.groceries.models import Grocery

UserModel = get_user_model()


class Review(models.Model):
    MAX_REVIEW_LEN = 255
    MIN_REVIEW_LEN = 10

    review = models.TextField(
        max_length=MAX_REVIEW_LEN,
        validators=[
            validators.MinLengthValidator(MIN_REVIEW_LEN)
        ],
        null=False,
        blank=False,
    )

    customer_rating = models.FloatField(
        validators=[
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5),
        ],
        null=False,
        blank=False,
    )

    grocery = models.ForeignKey(
        Grocery,
        on_delete=models.RESTRICT,
        related_name='reviews',
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )