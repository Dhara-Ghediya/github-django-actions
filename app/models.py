from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=25)
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    phone_no = models.IntegerField()
    email_id = models.EmailField(max_length=100, null=False, unique=True)
    
    def __str__(self):
        return self.username