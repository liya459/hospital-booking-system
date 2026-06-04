from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_decription = models.TextField()

    def __str__(self):
        return self.dep_name


class Doctor(models.Model):
   
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.doc_name


class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=100)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date = models.DateField()
    
    TIME_CHOICES = [
        ('09:00 AM', '09:00 AM - 10:00 AM'),
        ('10:00 AM', '10:00 AM - 11:00 AM'),
        ('11:00 AM', '11:00 AM - 12:00 PM'),
        ('02:00 PM', '02:00 PM - 03:00 PM'),
        ('03:00 PM', '03:00 PM - 04:00 PM'),
    ]
    booking_time = models.CharField(max_length=20, choices=TIME_CHOICES, default='09:00 AM')
    
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"Patient: {self.p_name} | Dr. {self.doc_name.doc_name}"