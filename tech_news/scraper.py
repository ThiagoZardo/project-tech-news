import requests
from parsel import Selector
import time


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
