from parsel import Selector
import requests
import time
from tech_news.database import create_news


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
    return Selector(html_content).css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("li.meta-author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").re_first(r"\d+")
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css(".label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    html_content = fetch("https://blog.betrybe.com/")
    news_list = scrape_updates(html_content)
    news_contents = []

    while amount > len(news_list):
        html_content = fetch(scrape_next_page_link(html_content))
        news_list.extend(scrape_updates(html_content))

    for news in news_list:
        html_content = fetch(news)
        news_contents.append(scrape_news(html_content))

    create_news(news_contents[:amount])

    return news_contents[:amount]
