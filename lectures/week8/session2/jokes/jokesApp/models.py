from django.db import models
import re
from django.db.models.deletion import CASCADE

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'
        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

class Joke(models.Model):
    question = models.TextField()
    punchline = models.TextField()
    user = models.ForeignKey(User, related_name='theUser', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)