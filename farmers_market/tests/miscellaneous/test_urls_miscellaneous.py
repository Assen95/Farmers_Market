from django.test import SimpleTestCase
from django.urls import reverse, resolve

from farmers_market.miscellaneous.views import AllGroceryListView, IndexView, basic_grocery_details, review_grocery, \
    AllCompanyListView


class TestMiscellaneousUrls(SimpleTestCase):

    def test_grocery_list_url_is_resolved(self):
        url = reverse('grocery list')
        self.assertEqual(resolve(url).func.view_class, AllGroceryListView)

    def test_index_view_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_basic_details_grocery_url_is_resolved(self):
        url = reverse('basic details view', args=['grocery_slug'])
        self.assertEqual(resolve(url).func, basic_grocery_details)

    def test_review_url_is_resolved(self):
        url = reverse('review grocery', args=['grocery_id'])
        self.assertEqual(resolve(url).func, review_grocery)

    def test_companies_list_url_is_resolved(self):
        url = reverse('company list')
        self.assertEqual(resolve(url).func.view_class, AllCompanyListView)