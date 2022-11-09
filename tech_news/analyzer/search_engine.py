from tech_news.database import (
    search_news
)


# Requisito 6
def search_by_title(title):
    list_news = []
    newlastter = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    for new in newlastter:
        list_news.append((new['title'], new['url']))

    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
