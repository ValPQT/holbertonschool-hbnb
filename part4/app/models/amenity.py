from app.models.base_model import BaseModel
from app import db


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(36), nullable=False)

    def __init__(self, name):
        super().__init__()
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) > 50:
            raise ValueError("name must be at most 50 characters")
        self.name = name
