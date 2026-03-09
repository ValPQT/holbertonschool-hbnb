#!/usr/bin/python3
"""
Module for the Place class.
"""
from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place or accommodation available in the application.
    """

    def __init__(self, title, description, price, latitude, longitude, owner_id):
        """
        Initialize a new Place instance.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self._owner = None
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        """Getter for title."""
        return self._title

    @title.setter
    def title(self, value):
        if not value or len(value) > 100:
            raise ValueError(
                "Title is required and must be under 100 characters")
        self._title = value

    @property
    def description(self):
        """Getter for description"""
        return self._description

    @description.setter
    def description(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Description must be a string")
            if len(value) > 500:
                raise ValueError("Description too long")
        self._description = value

    @property
    def price(self):
        """Getter for price."""
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a positive value")
        self._price = float(value)

    @property
    def latitude(self):
        """Getter for latitude."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, (int, float)) or not (-90.0 <= value <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        self._latitude = float(value)

    @property
    def longitude(self):
        """Getter for longitude."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (int, float)) or not (-180.0 <= value <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")
        self._longitude = float(value)

    @property
    def owner(self):
        """Getter for owner."""
        return self._owner

    @owner.setter
    def owner(self, value):
        if value is None:
            raise ValueError("Place must have a valid owner")
        self._owner = value

    def add_review(self, review):
        """Add a review to the place's list of reviews."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place's list of amenities."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
