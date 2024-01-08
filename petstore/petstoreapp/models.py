from django.db import models

# Create your models here.
class Pet(models.Model):
    petid = models.IntegerField(primary_key=True)
    petname = models.CharField(max_length=50)
    options = (("male", "male"), ("female", "female"))
    petgender = models.CharField(choices=options, default="", max_length=20)
    petage = models.IntegerField(null = False)
    petdescription = models.TextField(max_length = 200)
    petphoto = models.ImageField(upload_to="images")