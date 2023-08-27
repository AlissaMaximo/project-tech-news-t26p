from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)

        outcome = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )

        if outcome.status_code == 200:
            return outcome.text
        else:
            return None

    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    return (
        Selector(text=html_content)
        .css(".entry-preview .entry-title a::attr(href)")
        .getall()
    )


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
