from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views


from farmers_market.companies.forms import BaseCompanyForm, CompanyDeleteForm
from farmers_market.companies.models import Company
from farmers_market.groceries.models import Grocery

UserModel = get_user_model()


@login_required
def add_company(request):
    if request.method == 'GET':
        form = BaseCompanyForm(request.FILES)
    else:
        form = BaseCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'company/add-company.html', context)


# TODO: DoesNotExist
def view_company(request, pk):
    company = Company.objects.filter(user_id=pk).get()
    is_owner = request.user = company.user
    grocery_count = Grocery.objects.filter(pk=pk).count()
    has_company = Company.objects.filter(user_id=request.user.pk)

    context = {
        'company': company,
        'is_owner': is_owner,
        'grocery_count': grocery_count,
        'has_company': has_company,
    }

    return render(request, 'company/details-company.html', context)


@login_required
def edit_company(request, pk):
    company = Company.objects.filter(pk=pk).get()
    has_company = Company.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        form = BaseCompanyForm(instance=company)
    else:
        form = BaseCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('details company', pk=request.user.pk)

    context = {
        'form': form,
        'company': company,
        'has_company': has_company,
    }

    return render(request, 'company/edit-company.html', context)


def delete_company(request, pk):
    company = Company.objects.filter(pk=pk).get()
    has_company = Company.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        form = CompanyDeleteForm(instance=company)
    else:
        form = CompanyDeleteForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'company': company,
        'has_company': has_company,
    }

    return render(request, 'company/delete-company.html', context)
