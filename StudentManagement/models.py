from django.db import models
from django.contrib.auth.models import User

# Django automatically creates an id field in every model class and sets it as the primary key by default.
#The Parent Class Should be above the base class but if you cant do that pass the args as 'String'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Teacher(models.Model):
    teacherID = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length= 255)
    phoneNo = models.CharField(max_length= 255)
    position = models.CharField(max_length= 255)

    def __str__(self) -> str:                 #For returning the name of the teacher instead of original object string representation
        return self.name
    
    class Meta:                               #For Sorting the table according to the teachers ID
        ordering = ['teacherID']


class Student(models.Model):
    regNo = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length= 255)
    rollNo = models.SmallIntegerField()
    phoneNo = models.CharField(max_length=10, default="None")
    address = models.CharField(max_length= 255)
    YEAR_CHOICES = [
        ('FE', 'First Year'),
        ('SE', 'Second Year'),
        ('TE', 'Third Year'),
        ('BE', 'Fourth Year'),
    ]
    DIVISION_CHOICES = [(i, f"Division {i}") for i in range(1, 9)]    #8 sem hota ha engineering ma
    year = models.CharField(max_length=2, choices=YEAR_CHOICES, default='FE')
    division = models.IntegerField(choices=DIVISION_CHOICES, default=1)
    UPI_HANDLE_CHOICES = [
        ('@oksbi', '@oksbi'),
        ('@okhdfc', '@okhdfc'),
        ('@okicici', '@okicici'),
        ('@okaxis', '@okaxis'),
        ]
    upiId = models.CharField(max_length=50)  # For UPI ID before the '@'
    upiHandle = models.CharField(max_length=10, choices=UPI_HANDLE_CHOICES, default='@oksbi')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['regNo']


class Group(models.Model):
    groupId = models.BigAutoField(primary_key= True)      
    groupName = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups')
    students = models.ManyToManyField(Student, related_name='groups')
    
class Seller(models.Model):
    seller_ID = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)


class Announcement(models.Model):
    announcement = models.CharField(max_length= 255)
    timestamp = models.DateTimeField(auto_now_add= True)
    enddate = models.DateField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='announcements')


class Calender(models.Model):
    event = models.CharField(max_length= 255)
    eventTime = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='events')
    students = models.ManyToManyField(Student, related_name='events_viewable')


class SharingIsCaringStore(models.Model):
    price = models.SmallIntegerField()
    bookName = models.CharField(max_length= 255)
    image = models.ImageField(upload_to='images/')  # Customize the upload path...This argument specifies the directory within your media root where uploaded images will be saved. You'll need to configure your media settings in settings.py
    seller = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='books_sold')
    buyer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='books_bought', null=True, blank=True)


class Stationary(models.Model):
    itemName = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits= 6, decimal_places= 2)
    #seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='stationery_items') It should return all the books that are being bought from the stationary by a particular student


class ToDoList(models.Model):
    taskID = models.SmallIntegerField()
    taskName = models.CharField(max_length= 255)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)    #Each student has 1 TodoList

