from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'recipes'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.password = data['password']
        self.createdAt = data['createdAt']
        self.updatedAt = data['updatedAt']

    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        user_data = connectToMySQL(DB).query_db(query)

        users = []
        for user in user_data:
            users.append(cls(user))

        return users

    @classmethod
    def get_by_id(cls, user_id):

        data = {"id": user_id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_email(cls,email):

        data = {
            "email": email
        }
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user (firstName, lastName, email, password) VALUES (%(firstName)s, %(lastName)s, %(email)s, %(password)s);'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass

# Validate the registration input:
    @staticmethod
    def validate(user):
        isValid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        if len(results) >= 1:
            isValid = False
            flash("Email is already in use in our database")
        if len(user['firstName']) < 2:
            isValid = False
            flash("Please use least least 2 characters for the first Name")
        if len(user['lastName']) < 2:
            isValid = False
            flash("Please use least least 2 characters for the last Name")
        if len(user['password']) < 6:
            isValid = False
            flash("Please use least least 6 characters for the password")
        if not EMAIL_REGEX.match(user['email']):
            isValid = False
            flash("Please use proper email format")
        if user['password'] != user['confirm']:
            isValid = False
            flash("Passwords don't match")
        return isValid