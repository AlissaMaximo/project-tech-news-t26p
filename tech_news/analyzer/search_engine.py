from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    found_news = db.news.find({"title": {"$regex": title, "$options": "i"}})

    return [(news["title"], news["url"]) for news in found_news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        object_data = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    formatted_date = object_data.strftime("%d/%m/%Y")
    dates = list(
        db.search_news(
            {"timestamp": formatted_date},
            {"title": True, "url": True, "_id": False},
        )
    )

    return [(noticia["title"], noticia["url"]) for noticia in dates]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
