from django.test import TestCase, Client
from django.urls import reverse

from farmers_market.accounts.models import AppUser
from farmers_market.companies.models import Company


class TestCompanyView(TestCase):
    def setUp(self):
        self.client = Client()
        self.company_detail_url = reverse('details company', args=[1])
        self.company_add_url = reverse('add company')
        self.user1 = AppUser.objects.create(
            username='asen123',
            email='asen123',
        )
        self.company1 = Company.objects.create(
            name='test_company',
            logo='image',
            location='place1',
            date_formed='2000-12-15',
            user=self.user1,
        )

    def test_company_detail_get_correctly(self):
        response = self.client.get(self.company_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company/details-company.html')

    def test_company_add_post_correctly_and_gets_correct_pk(self):
        response = self.client.post(self.company_add_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.company1.name, 'test_company')
        self.assertEqual(self.company1.pk, self.user1.pk)

