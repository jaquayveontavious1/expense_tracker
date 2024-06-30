from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Expense Model
class Expenses(models.Model) :
    #Choices in the category column
    CATEGORY_CHOICES = [
        ('groceries','Groceries'),
        ('transport','Transport'),
        ('entertainment','Entertainment'),
        ('loans','Loans'),
        ('food','Food'),
        ('insurance','Insurance'),
        ('travel','Travel'),
        ('rent','Rent')
    
    ]
    username = models.ForeignKey(User,on_delete=models.CASCADE)#has a foreignkey so that each diff user access their own info
   
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES)
    description = models.TextField(max_length=255)

    class Meta :
        ordering = ['-date']
    def __str__ (self) :
        return(f"{self.username} - {self.amount} on {self.amount} with {self.category}")

class Register(models.Model) :
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pasword = models.CharField(max_length=50)

    def __str__ (self) :
        return(f"{self.username} {self.email}")


class Login(models.Model) :
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self) :
        return(f"{self.username}")

class Logout(models.Model) :
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self) :
        return(f"{self.username}")
    




