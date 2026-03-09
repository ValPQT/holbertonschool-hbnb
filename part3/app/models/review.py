#!/usr/bin/python3
"""
Module for the Review class.
This module defines the Review class which inherits from BaseModel.
"""
from app.models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place.

    Attributes:
        text (str): The content of the review.
        rating (int): The rating given to the place (1-5).
        place (Place): The Place instance associated with the review.
        user (User): The User instance who wrote the review.
    """

    def __init__(self, text, rating, place, user):
        """
        Initializes a new Review instance.

        Args:
            text (str): The review's content.
            rating (int): Numerical rating from 1 to 5.
            place (Place): The place being reviewed.
            user (User): The author of the review.
        """
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        """str: Get or set the content of the review."""
        return self._text

    @text.setter
    def text(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("The content of the review is mandatory")
        self._text = value

    @property
    def rating(self):
        """int: Get or set the rating (must be between 1 and 5)."""
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("The rating must be an integer between 1 and 5")
        self._rating = value

    @property
    def place(self):
        """Place: Get or set the Place linked to this review."""
        return self._place

    @place.setter
    def place(self, value):
        if value is None:
            raise ValueError("The review must be linked to a valid Place")
        self._place = value

    @property
    def user(self):
        """User: Get or set the User who authored this review."""
        return self._user

    @user.setter
    def user(self, value):
        if value is None:
            raise ValueError("The review must have a valid author(User)")
        self._user = value
