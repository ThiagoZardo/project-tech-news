from datetime import datetime
from tech_news.database import (search_news)


# Requisito 6
def search_by_title(title):
    list_news = []
    newlastter = search_news(
        {'title': {'$regex': title, '$options': 'i'}}
    )
    for new in newlastter:
        list_news.append((new['title'], new['url']))

    return list_news


# Requisito 7
def search_by_date(date):
    try:
        format_data = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
        list_news = []
        newlastter = search_news({'timestamp': format_data})
        for new in newlastter:
            list_news.append((new['title'], new['url']))

        return list_news
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    list_news = []
    newlastter = search_news(
        {'tags': {'$elemMatch': {'$regex': tag, '$options': 'i'}}}
    )
    for new in newlastter:
        list_news.append((new['title'], new['url']))

    return list_news


# Requisito 9
def search_by_category(category):
    list_news = []
    newlastter = search_news(
        {'category': {'$regex': category, '$options': 'i'}}
    )
    for new in newlastter:
        list_news.append((new['title'], new['url']))

    return list_news
