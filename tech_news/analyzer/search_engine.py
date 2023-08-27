from tech_news.database import db


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    found_news = db.news.find({"title": {"$regex": title, "$options": "i"}})

    return [(news["title"], news["url"]) for news in found_news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
