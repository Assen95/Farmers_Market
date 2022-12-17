from django.shortcuts import render, redirect
from django.views import generic as view

from farmers_market.companies.models import Company
from farmers_market.news.forms import AddNewsForm, EditNewsForm, DeleteNewsForm
from farmers_market.news.models import News
from farmers_market.news.utils import get_news_by_news_id_and_author_id


def add_news(request):
    if request.method == 'GET':
        form = AddNewsForm(request.FILES)
    else:
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'news/add-news.html', context)


class AllNewsListView(view.ListView):
    template_name = 'news/news-dashboard.html'
    model = News
    context_object_name = 'newses'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_company'] = Company.objects.filter(user_id=self.request.user.pk)

        return context


def view_news(request, news_id):
    news = News.objects.filter(pk=news_id).get()
    is_owner = request.user = news.author
    has_company = Company.objects.filter(user_id=request.user.pk)

    context = {
        'news': news,
        'is_owner': is_owner,
        'has_company': has_company,
    }

    return render(request, 'news/details-news.html', context)


def edit_news(request, author_id, news_id):
    news = get_news_by_news_id_and_author_id(news_id, author_id)
    has_company = Company.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        form = EditNewsForm(instance=news)
    else:
        form = EditNewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news list')

    context = {
        'form': form,
        'news': news,
        'has_company': has_company,
    }

    return render(request, 'news/edit-news.html', context)


def delete_news(request, author_id, news_id):
    news = get_news_by_news_id_and_author_id(news_id, author_id)
    has_company = Company.objects.filter(user_id=request.user.pk)
    if request.method == 'GET':
        form = DeleteNewsForm(instance=news)
    else:
        form = DeleteNewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news list')

    context = {
        'news': news,
        'form': form,
        'has_company': has_company,
    }

    return render(request, 'news/delete-news.html', context)
