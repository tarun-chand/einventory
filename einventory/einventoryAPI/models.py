from tkinter import CASCADE
from django.db import models

# Create your models here.


class ProductTypeMaster(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    product_type_name = models.CharField(max_length=250)
    entry_date = models.DateField()

    def __str__(self):
        return self.product_type_name


class BuildingMaster(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=250)
    entry_date = models.DateField()

    def __str__(self):
        return self.building_name


class Product_details(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(
        ProductTypeMaster, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_model = models.CharField(max_length=250)
    product_serialno = models.CharField(max_length=250)
    product_notsheet_no = models.CharField(max_length=250)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    entry_date = models.DateField()


class User_details(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=250)
    post = models.CharField(max_length=250)
    mobileno = models.IntegerField()
    entry_date = models.DateField()


class Section_details(models.Model):
    section_id = models.AutoField(primary_key=True)
    building_name = models.ForeignKey(BuildingMaster, on_delete=models.CASCADE)
    floor = models.CharField(max_length=250)
    roomno = models.CharField(max_length=250)
    section_name = models.CharField(max_length=250)
    entry_date = models.DateField()


class Allotment_details(models.Model):
    allot_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    curr_loc = models.IntegerField()
    prev_loc = models.IntegerField()
    status = models.CharField(max_length=50, choices=(
        ('Working', 'Working'), ('Not Working', 'Not Working')))
    remarks = models.CharField(max_length=250)
    allot_date = models.DateField()
