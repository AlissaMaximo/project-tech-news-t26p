import pytest
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import Mock, patch


mock_data = [
    {
        "title": "Não deixe para depois: Python é a linguagem"
        "mais quente do momento",
        "reading_time": 4,
    },
    {
        "title": "Selenium, BeautifulSoup ou Parsel?" "Entenda as diferenças",
        "reading_time": 3,
    },
    {
        "title": "Pytest + Faker: a combinação poderosa dos testes!",
        "reading_time": 10,
    },
    {
        "title": "FastAPI e Flask: frameworks para APIs em Python",
        "reading_time": 15,
    },
    {
        "title": "A biblioteca Pandas e o sucesso da linguagem Python",
        "reading_time": 12,
    },
]

expected_output = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Não deixe para depois: Python é a linguagem"
                    "mais quente do momento",
                    4,
                ),
                (
                    "Selenium, BeautifulSoup ou Parsel?"
                    "Entenda as diferenças",
                    3,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Pytest + Faker: a combinação poderosa dos testes!",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("FastAPI e Flask: frameworks para APIs em Python", 15),
        ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
    ],
}


def test_reading_plan_group_news():
    mock_find_news = Mock(return_value=mock_data)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mock_find_news,
    ):
        assert (
            ReadingPlanService.group_news_for_available_time(10)
            == expected_output
        )
