from typing import List

from pydantic import BaseModel

book_store_get_books = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "books": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "isbn": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "subTitle": {
                            "type": "string"
                        },
                        "author": {
                            "type": "string"
                        },
                        "publish_date": {
                            "type": "string"
                        },
                        "publisher": {
                            "type": "string"
                        },
                        "pages": {
                            "type": "integer"
                        },
                        "description": {
                            "type": "string"
                        },
                        "website": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "isbn",
                        "title",
                        "subTitle",
                        "author",
                        "publish_date",
                        "publisher",
                        "pages",
                        "description",
                        "website"
                    ]
                }
            ]
        }
    },
    "required": [
        "books"
    ]
}


class Book(BaseModel):
    isbn: int
    title: int
    subTitle: int
    author: str
    publish_date: str
    publisher: str
    pages: int
    description: str
    website: str


class BooksModel(BaseModel):
    books: List[Book]