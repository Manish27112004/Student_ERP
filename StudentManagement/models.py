from django.db import models

# Django automatically creates an id field in every model class and sets it as the primary key by default.
#The Parent Class Should be above the base class but if you cant do that pass the args as 'String'


class Teacher(models.Model):
    teacherID = models.SmallIntegerField(primary_key= True)
    name = models.CharField(max_length= 255)
    phoneNo = models.BigIntegerField()
    position = models.CharField(max_length= 255)


class Student(models.Model):
    regNo = models.SmallIntegerField(primary_key= True)
    name = models.CharField(max_length= 255)
    rollNo = models.SmallIntegerField()
    phoneNo = models.BigIntegerField()
    address = models.CharField(max_length= 255)
    sem = models.SmallIntegerField()
    classStudying = models.CharField()


class Announcement(models.Model):
    announcement = models.CharField(max_length= 255)
    timestamp = models.DateTimeField()
    

class Calender(models.Model):
    event = models.CharField(max_length= 255)
    eventTime = models.DateTimeField()


class SharingStore(models.Model):
    price = models.SmallIntegerField()
    bookName = models.CharField(max_length= 255)
    image = models.ImageField(upload_to='images/')  # Customize the upload path...This argument specifies the directory within your media root where uploaded images will be saved. You'll need to configure your media settings in settings.py


class Stationary(models.Model):
    itemName = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits= 6, decimal_places= 2)


class ToDoList(models.Model):
    taskID = models.SmallIntegerField()
    taskName = models.CharField(max_length= 255)


