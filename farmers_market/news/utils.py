from farmers_market.news.models import News


def get_news_by_news_id_and_author_id(news_id, author_id):
    return News.objects \
        .filter(id=news_id, author_id=author_id) \
        .get()