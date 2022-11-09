import requests
from parsel import Selector
import time
from tech_news.database import (
    create_news
)


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    cards = []

    for card in selector.css('div.cs-overlay'):
        text = card.css('a::attr(href)').get()
        cards.append(text)
    return cards


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    url = selector.css('a.next::attr(href)').get()
    return url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css('link[rel=canonical]::attr(href)').get()
    title = selector.css('.entry-title::text').get().strip()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('a.url.fn.n::text').get() or 0
    tags = selector.css('.post-tags > ul > li > a::text').getall()
    summary = selector.css(
        '.entry-content > p:nth-of-type(1) *::text').getall()
    comments_count = len(selector.css('.comment-author').getall())
    category = selector.css('span.label::text').get()

    articles = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'comments_count': comments_count,
        'summary': "".join(summary).strip(),
        'tags': tags,
        'category': category,
    }
    return articles


# Requisito 5
def get_tech_news(amount):
    list_news = []
    list_newsletter = []
    url = 'https://blog.betrybe.com'
    while len(list_news) < amount:
        html_content = fetch(url)
        list_news.extend(scrape_novidades(html_content))
        url = scrape_next_page_link(html_content)
    for new in list_news[:amount]:
        newsletter = fetch(new)
        list_newsletter.append(scrape_noticia(newsletter))
    create_news(list_newsletter)
    return list_newsletter
