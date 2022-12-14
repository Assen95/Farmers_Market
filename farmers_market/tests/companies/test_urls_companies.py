from django.test import SimpleTestCase
from django.urls import reverse, resolve

from farmers_market.companies.views import add_company, view_company, edit_company, delete_company


class TestCompanyUrls(SimpleTestCase):

    def test_company_add_url_is_resolved(self):
        url = reverse('add company')
        self.assertEqual(resolve(url).func, add_company)

    def test_company_view_url_is_resolved(self):
        url = reverse('details company', args=[1])
        self.assertEqual(resolve(url).func, view_company)

    def test_company_edit_url_is_resolved(self):
        url = reverse('edit company', args=[1])
        self.assertEqual(resolve(url).func, edit_company)

    def test_company_delete_url_is_resolved(self):
        url = reverse('delete company', args=[1])
        self.assertEqual(resolve(url).func, delete_company)
