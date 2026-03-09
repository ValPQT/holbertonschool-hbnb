from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """id (String): Unique identifier for each amenity.
    name (String): The name of the amenity (e.g., "Wi-Fi", "Parking").
    Required, maximum length of 50 characters.
    created_at (DateTime): Timestamp when the amenity is created.
    updated_at (DateTime): Timestamp when the amenity is last updated"""

    def __init__(self, name):
        super().__init__()

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if len(name) > 50:
            raise ValueError("name must be at most 50 characters")

        self.name = name
        self.places = []

    def add_place(self, place):
        self.places.append(place)


list_equipement = ["Wi-Fi", "Air Conditioning","Parking"]

amenities = [Amenity(name) for name in list_equipement]


def create_amenity(self, amenity_data):
    # Placeholder for logic to create an amenity
    new_amenity = Amenity(name=amenity_data['name'])

    self.amenity_repo.add(new_amenity)

    return new_amenity


def add(self, obj):
    self._items.append(obj)


def get(self, obj_id):
    for obj in self._items:
        if obj.id == obj_id:
            return obj
        raise ValueError("Object not found")


def get_all(self):
    return self._items


def update(self, obj_id, data: dict):
    obj = self.get(obj_id)
    if not obj:
        raise ValueError("Amenity not found")

    for key, value in data.items():
        if key != "id" and hasattr(obj, key):
            setattr(obj, key, value)
        return obj

def to_dict(self):
    return {'id': self.id, 'name': self.name}
