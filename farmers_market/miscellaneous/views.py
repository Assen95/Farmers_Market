from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as view

from farmers_market.companies.models import Company
from farmers_market.groceries.models import Grocery
from farmers_market.miscellaneous.forms import ReviewGroceryForm
from farmers_market.miscellaneous.models import Review

UserModel = get_user_model()


class IndexView(view.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserModel.objects.filter(pk=self.request.user.pk)
        context['has_company'] = Company.objects.filter(user_id=self.request.user.pk)
        return context


class AllGroceryListView(view.ListView):
    template_name = 'common/dashboard.html'
    model = Grocery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groceries'] = Grocery.objects.all()
        context['has_company'] = Company.objects.filter(user_id=self.request.user.pk)
        return context


class AllCompanyListView(view.ListView):
    template_name = 'common/companies-dashboard.html'
    model = Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = Company.objects.all()
        context['has_company'] = Company.objects.filter(user_id=self.request.user.pk)
        return context


# class BasicGroceryDetails(view.DetailView):
#     model = Grocery
#     template_name = 'common/basic-details-grocery.html'
#     context_object_name = 'grocery'
#     slug_field = 'slug'
#     slug_url_kwarg = 'grocery_slug'
#
#     def get_context_data(self, **kwargs):
#         context = super(BasicGroceryDetails, self).get_context_data(**kwargs)
#         context['grocery'] = Grocery.objects.filter(slug=self.slug_field).get()
#         context['has_company'] = Company.objects.filter(user_id=self.request.user.pk)
#         return context

def basic_grocery_details(request, grocery_slug):
    grocery = Grocery.objects.filter(slug=grocery_slug).get()
    reviews = Review.objects.filter(user=request.user.pk).all()

    context = {
        'grocery': grocery,
        'review_form': ReviewGroceryForm(),
        'reviews': reviews,
    }

    return render(request, 'common/basic-details-grocery.html', context)


@login_required
def review_grocery(request, grocery_id):
    grocery = Grocery.objects.filter(pk=grocery_id).get()

    form = ReviewGroceryForm(request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.grocery = grocery
        review.save()

    return redirect('grocery list')


def about_us_page(request):
    has_company = Company.objects.filter(user_id=request.user.pk)

    context = {
        'has_company': has_company,
    }

    return render(request, 'common/about-us.html', context)
