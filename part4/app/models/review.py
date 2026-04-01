from app.models.base_model import BaseModel
from app import db


class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)

    # Relations
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))

    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("The content of the review is mandatory")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not (1 <= value <= 5):
            raise ValueError("The rating must be an integer between 1 and 5")
        self._rating = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if value is None:
            raise ValueError("The review must be linked to a valid Place")
        self._place = value
        self.place_id = value.id

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if value is None:
            raise ValueError("The review must have a valid author(User)")
        self._user = value
        self.user_id = value.id