from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
    Thriller = "Thriller"
    Romance = "Romance"
    Poetry = "Poetry"
    Horror = "Horror"
    Cookbooks = "Cookbooks"
    Adventure = "Adventure"
    Technology = "Technology"
    History = "History"
    Philosophy = "Philosophy"
    Fantasy = "Fantasy"

############################################
# Classes are defined here
############################################
class AuthorCreate(BaseModel):
    birth: date
    name: str
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class LibraryCreate(BaseModel):
    web_page: str
    telephone: str
    name: str
    address: str
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class BookCreate(BaseModel):
    stock: int
    genre: Genre
    price: float
    pages: int
    title: str
    release: date
    library: List[int]  # N:M Relationship
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

