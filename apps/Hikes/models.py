
from django.db import models
import re
import datetime
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
todays_date = datetime.date.today()


class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['firstName']) < 3 or not postData['firstName'].isalpha():
            errors['firstName'] = 'Please enter a first name'
        if len(postData['lastName']) < 3 or not postData['lastName'].isalpha():
            errors['lastName'] = 'Please enter a last name'
        if len(postData['email']) < 1:
            errors['email'] = "Please enter an email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] ='Password must contain 8 characters'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password'] = 'Password must contain at least one uppercase and one number'
        if postData['password'] != postData['confirmPassword']:
            errors['confirmPassword'] = "Passwords do not match"
        print(errors)
        return errors

    def loginValidator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid Email"
        return errors
        
        # user = User.objects.filter(email = postData['email'])
        # errors = {}
        # if not user:
        #     errors['email'] = "Please enter a valid email"
        # if user and not bcrypt.checkpw(postData['password'].encode('utf-8'),user[0].password.encode('utf-8')):
        #     print('password dont match')
        #     errors['password'] = "Invalid password"
        # return errors



class User(models.Model):
    firstName = models.CharField(max_length=155)
    lastName = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    password = models.CharField(max_length=255)
    rattleSnake = models.IntegerField(default=0)
    littleSi = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = userManager()

# class Vote(models.Model):
#     user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
#     votes = models.ManyToManyField(User, related_name= "votes", blank = True)
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     objects = userManager()
