from app.persistence.repository import SQLAlchemyRepository

"""This class will handle communication between the Presentation,
Business Logic, and Persistence layers. You will interact with the repositories
(like the in-memory repository) through this Class:"""

from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repository = SQLAlchemyRepository(User)
        self.place_repository = SQLAlchemyRepository(Place)
        self.review_repository = SQLAlchemyRepository(Review)
        self.amenity_repository = SQLAlchemyRepository(Amenity)

    # ---------------- User Methods ----------------
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repository.add(user)
        return user

    def get_user_by_id(self, user_id):
        return self.user_repository.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repository.get_by_attribute("email", email)

    def get_all_users(self):
        return self.user_repository.get_all()

    def update_user(self, user_id, user_data):
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        for key, value in user_data.items():
            setattr(user, key, value)
        return user

    # ---------------- Amenity Methods ----------------
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        updated = self.amenity_repository.update(amenity_id, amenity_data)
        if not updated:
            raise ValueError("Amenity not found")
        return updated

    # ---------------- Place Methods ----------------
    def create_place(self, place_data):
        owner_id = place_data.get("owner_id")
        owner = self.user_repository.get(owner_id)
        if not owner:
            raise ValueError("Owner not found")

        amenity_ids = place_data.pop("amenities", [])

        new_place = Place(**place_data)
        new_place.owner = owner

        for amenity_id in set(amenity_ids):
            amenity = self.amenity_repository.get(amenity_id)
            if amenity:
                new_place.add_amenity(amenity)
            else:
                raise ValueError(f"Amenity '{amenity_id}' not found")

        self.place_repository.add(new_place)
        return new_place

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            setattr(place, key, value)
        return place

    # ---------------- Review Methods ----------------
    def create_review(self, review_data):
        user = self.user_repository.get(review_data.get("user_id"))
        place = self.place_repository.get(review_data.get("place_id"))

        if not user or not place:
            raise ValueError("User or Place not found")

        review = Review(
            text=review_data["text"],
            rating=review_data["rating"],
            user=user,
            place=place
        )

        self.review_repository.add(review)
        place.add_review(review)
        return review

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repository.get(place_id)
        if not place:
            return None
        return getattr(place, "reviews", [])

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            return None
        allowed_fields = ["text", "rating"]
        for key in allowed_fields:
            if key in review_data:
                setattr(review, key, review_data[key])
        return review

    def delete_review(self, review_id):
        review = self.review_repository.get(review_id)
        if not review:
            return False
        if hasattr(review, "place") and review.place:
            review.place.reviews = [
                r for r in review.place.reviews if r.id != review_id
            ]
        self.review_repository.delete(review_id)
        return True
