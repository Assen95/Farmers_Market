from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
import json
from farmers_market.accounts.models import AppUser
from farmers_market.companies.models import Company
from farmers_market.groceries.models import Grocery, Category


class TestMiscellaneousView(TestCase):
    def setUp(self):
        self.client = Client()
        self.grocery_list_urls = reverse('grocery list')
        self.index_url = reverse('index')
        self.company_list_url = reverse('company list')
        # self.basic_grocery_details_url = reverse('basic details view', args=[f'grocery-1'])
        # self.category1 = Category.objects.create(
        #     name='Fish',
        # )
        # self.user1 = AppUser.objects.create(
        #     username='asen1',
        #     email='asen1@email.com',
        # )
        # self.company1 = Company.objects.create(
        #     name='company1',
        #     logo='image',
        #     location='place1',
        #     date_formed='2000-12-15',
        #     user=self.user1,
        # )
        # self.grocery1 = Grocery.objects.create(
        #     name='grocery',
        #     category=self.category1,
        #     quality_rating=5,
        #     expiry_date='2022-12-15',
        #     image_url='image',
        #     user=self.user1,
        #     company=self.company1,
        # )

    def test_miscellaneous_all_grocery_list_get(self):
        response = self.client.get(self.grocery_list_urls)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/dashboard.html')

    def test_miscellaneous_index_get(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-page.html')

    def test_miscellaneous_company_list_get(self):
        response = self.client.get(self.company_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/companies-dashboard.html')

    # def test_miscellaneous_basic_grocery_details_get(self):
    #     response = self.client.get(self.basic_grocery_details_url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'common/basic-details-grocery.html')
