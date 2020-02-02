from django.db import models

# Create your models here.
class add_idea11(models.Model):
    title = models.TextField(max_length=200)
    domain = models.TextField(max_length=200)
    ncollab = models.IntegerField()
    link = models.TextField(max_length=300)
    about = models.TextField(max_length=1000)
    nlike = models.IntegerField()
    nviews = models.IntegerField()
    email=models.TextField(max_length=30)

class user_profile11(models.Model):
    fname = models.TextField(max_length=200)
    lname = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    contact = models.IntegerField()
    password = models.TextField(max_length=200)
    qualification = models.TextField(max_length=500)
    address = models.TextField(max_length=300)
    city = models.TextField(max_length=200)
    country = models.TextField(max_length=200)
    postal_code = models.IntegerField()
    about_me = models.TextField(max_length=1000)
    
class register_user11(models.Model):
    name = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    contact = models.IntegerField()
    password = models.TextField(max_length=200)
    typeof = models.TextField(max_length=2)

class register_investor11(models.Model):
    company_name = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    gst_no = models.IntegerField()
    contact = models.IntegerField()
    password = models.TextField(max_length=200)
    typeof = models.TextField(max_length=2)
    
class watchlist1(models.Model):
    domain = models.TextField(max_length=200)
    title =  models.TextField(max_length=200)
    email = models.TextField(max_length=200)