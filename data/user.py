from datetime import datetime


class User:
    def __init__(self, name, email, hashed_password):
        self.id = 1
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.created_date: datetime = None
        self.profile_image_url = ""
        self.last_login_date: datetime = None
