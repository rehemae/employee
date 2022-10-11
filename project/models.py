from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=20, null=True)
    second_name = models.CharField(max_length=240, null=True)
    date_of_graduation=models.DateTimeField()
    date_of_employment=models.DateTimeField()
    POSITION_CHOICES=(
       ("H", "Human Resource"),
       ("C", "Chief executive officer"),
       ("M","Manager"),
       ("P","President"),
       ("P","Product Manager"),
       ("F","Finance Manager"),
       ("A","Accountant"),
        ("O","Others"),
   )
    position= models.CharField(max_length=30,choices=POSITION_CHOICES,null=True)
    salary=models.IntegerField()
    supervisors=models.CharField(max_length=20,null=True)

class Login(models.Model):
    user_name=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20,null=True)

    # def __str__(self):
    #  return self.first_name
