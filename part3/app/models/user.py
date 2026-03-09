from email_validator import validate_email, EmailNotValidError
from app.models.base_model import BaseModel
from app.__init__ import bcrypt

class User(BaseModel):
    def __init__(self, first_name, last_name, email):
        super().__init__()

        self.__first_name = None
        self.first_name = first_name

        self.__last_name = None
        self.last_name = last_name

        self.__email = None
        self.email = email

        self.is_admin = False
        self.reviews = []
        self.places = []

    # FIRST NAME
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value:
            raise ValueError("First name is required")
        self.__first_name = value

    # LAST NAME
    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value:
            raise ValueError("Last name is required")
        self.__last_name = value

    # EMAIL
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email is required")

        try:
            valid = validate_email(value, check_deliverability=False)
            self.__email = valid.normalized
        except EmailNotValidError:
            raise ValueError("Invalid email address format")

    # METHODS
    def add_review(self, review):
        self.reviews.append(review)

    def add_place(self, place):
        self.places.append(place)

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
