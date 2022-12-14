from django.test import TestCase

from farmers_market.accounts.models import AppUser
from farmers_market.miscellaneous.models import Review


class TestMiscellaneousModels(TestCase):
    def setUp(self):
        self.user1 = AppUser.objects.create(
            username='asen1',
            email='asen1@email.com',
            profile_picture='image'
        )
        self.review1 = Review.objects.create(
            review='Alabalanicaturskapanica',
            customer_rating=5,
            user=self.user1,
        )

    def test_review1_is_assigned_a_user_on_creation(self):
        self.assertEqual(self.review1.user, self.user1)