from django.db import models 
from django.conf import settings 
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Trainers(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)


class Athletes(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    
class Sports(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

class News(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(verbose_name="Дата события",
        help_text="Введите дату события",
        null=True,
        blank=True,
        default=timezone.now)

class Contact(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.CharField(max_length=3, db_index=True)
    sport = models.TextField()
    phone = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"