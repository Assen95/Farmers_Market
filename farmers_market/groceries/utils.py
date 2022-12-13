from farmers_market.groceries.models import Grocery


def get_grocery_by_slug_and_username(grocery_slug, username):
    return Grocery.objects \
        .filter(slug=grocery_slug, user__username=username) \
        .get()
