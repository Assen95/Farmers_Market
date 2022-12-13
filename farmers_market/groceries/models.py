from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

from farmers_market.companies.models import Company

'''
name, category(separate model), quality, date_created, expiry_date, foreign key(company)
'''

UserModel = get_user_model()


class Category(models.Model):
    MAX_NAME_LEN = 30

    name = models.CharField(
        max_length=MAX_NAME_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Grocery(models.Model):
    MAX_LEN_NAME = 30

    name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT,
    )

    quality_rating = models.FloatField(
        validators=[
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5),
        ]
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
    expiry_date = models.DateField()

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)
