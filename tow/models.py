from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_helpdesk = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)


class Towing(models.Model):
    vehicle_num = models.CharField(max_length=200, blank=True, primary_key=True)
    vehicle_type = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.vehicle_num


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=200, blank=True)
    user_contact = models.CharField(max_length=200, blank=True)
    user_role = models.CharField(max_length=200, blank=True)
    user_email = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    zip = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user_id


class Customer(models.Model):
    Customer_name = models.CharField(max_length=200, blank=True)
    Customer_contact = models.CharField(max_length=200, blank=True)
    Customer_email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Customer_name


class Incident(models.Model):
    incident_user_id = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    towing_vehicle_id = models.OneToOneField(Towing, on_delete=models.CASCADE)
    customer_id = models.OneToOneField(Customer, on_delete=models.CASCADE)
    Description = models.CharField(max_length=200, blank=True)
    estimated_distance = models.CharField(max_length=10, blank=True)
    estimated_price = models.CharField(max_length=10, blank=True)
    actual_distance = models.CharField(max_length=10, blank=True)
    actual_price = models.CharField(max_length=10, blank=True)
    date_time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.incident_user_id



