from django.shortcuts import render
from .models import *

# create user -> params (ftid, username, age, email, disclaimer)
# new User
# ftid = ftid
# username = username
# age = age
# email = email
# disclaimer = disclaimer
# save user in the database
#data = {"ftid":"4832", "username":"tarek", "email":"tarek@gmail.com", "age":12, "disclaimer":1}

def createUser(data):
    try:
        User.objects.create(ftid=data["ftid"], 
                            username=data["username"], 
                            email=data["email"], 
                            age=data["age"] or None, 
                            disclaimer=data["disclaimer"] or None)
    except KeyError:
        print("missing a required field.")
    except:
        print("invalid data entry.")
    return

def readUser(id):
    user = User.objects.get(id=id)
    return user

def updateUser(id, ftid=None, username=None, age=None, 
               email=None, disclaimer=None):
    user = User.objects.get(id=id)
    if ftid is not None:
        user.ftid = ftid
    if username is not None:
        user.username = username
    if age is not None:
        user.age = age
    if email is not None:
        user.email = email
    if disclaimer is not None:
        user.disclaimer = disclaimer
    user.save()
    return

def deleteUser(id):
    user = User.objects.get(id=id)
    user.delete()
    return