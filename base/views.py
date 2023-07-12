from django.shortcuts import render
from .models import User

# create user -> params (ftid, username, age, email, disclaimer)
# new User
# ftid = ftid
# username = username
# age = age
# email = email
# disclaimer = disclaimer
# save user in the database

def createUser(ftid, username, age, email, disclaimer):
    user = User(ftid=ftid, username=username, 
                age=age, email=email, 
                disclaimer=disclaimer)
    user.save()
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