from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as view

from farmers_market.companies.models import Company
from farmers_market.groceries.forms import AddGroceryForm, EditGroceryForm, DeleteGroceryForm
from farmers_market.groceries.models import Grocery
from farmers_market.groceries.utils import get_grocery_by_slug_and_username

UserModel = get_user_model()


@login_required
def add_grocery(request):
    has_company = Company.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        form = AddGroceryForm()
    else:
        form = AddGroceryForm(request.POST)
        if form.is_valid():
            grocery = form.save(commit=False)
            grocery.user = request.user
            grocery.save()
            return redirect('details company', pk=request.user.pk)

    context = {
        'form': form,
        'has_company': has_company,
    }

    return render(request, 'grocery/create-grocery.html', context)


class GroceryListView(LoginRequiredMixin, view.ListView):
    model = Grocery
    template_name = 'grocery/my-groceries.html'
    context_object_name = ' mygroceries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groceries'] = Grocery.objects.filter(user=self.request.user).all()
        context['has_company']= Company.objects.filter(user_id=self.request.user.pk)
        return context

    def get_queryset(self):
        return Grocery.objects.filter(
            user=self.request.user
        ).order_by('date_created')


def details_grocery(request, username, grocery_slug):
    grocery = get_grocery_by_slug_and_username(grocery_slug, username)
    has_company = Company.objects.filter(user_id=request.user.pk)

    context = {
        'grocery': grocery,
        'has_company': has_company,
    }
    return render(request, 'grocery/details-grocery.html', context)


def edit_grocery(request, username, grocery_slug):
    has_company = Company.objects.filter(user_id=request.user.pk)
    grocery = get_grocery_by_slug_and_username(grocery_slug, username)
    if request.method == 'GET':
        form = EditGroceryForm(instance=grocery)
    else:
        form = EditGroceryForm(request.POST, instance=grocery)
        if form.is_valid():
            form.save()
            return redirect('details grocery', username=username, grocery_slug=grocery_slug)

    context = {
        'form': form,
        'grocery_slug': grocery_slug,
        'username': username,
        'has_company': has_company,
    }

    return render(request, 'grocery/edit-grocery.html', context)


def delete_grocery(request, username, grocery_slug):
    has_company = Company.objects.filter(user_id=request.user.pk)
    grocery = get_grocery_by_slug_and_username(grocery_slug, username)

    if request.method == 'GET':
        form = DeleteGroceryForm(instance=grocery)
    else:
        form = DeleteGroceryForm(request.POST, instance=grocery)
        if form.is_valid():
            form.save()
            return redirect('details company', pk=request.user.pk)

    context = {
        'form': form,
        'username': username,
        'grocery_slug': grocery_slug,
        'has_company': has_company
    }

    return render(request, 'grocery/delete-grocery.html', context)
