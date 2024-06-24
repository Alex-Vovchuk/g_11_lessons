import requests
from jsonschema import validate

from real_project_example.helper.jsonschemas.book_store_schemas import book_store_get_books, BooksModel


def test_get_books():
    response = requests.get(
        url='https://demoqa.com/BookStore/v1/Books',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        },
        timeout=5
    )
    books_json = response.json()
    validate(books_json, book_store_get_books)
    BooksModel(**books_json)

# '13cb2622-bcaa-40de-a0a1-5c91a2637730'


def test_post_books():
    url_1 = 'https://demoqa.com//Account/v1/User'
    response = requests.post(
        url=url_1,
        json={"userName": "SecondUserG11", "password": "Volf1@vsf"}
    )
    token_dict = response.json()
