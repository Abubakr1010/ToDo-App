from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class User(models.Models):
    user_id = models.IntegerField(primary_key=True,validators=[MinValueValidator(1)])
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField(max_lenght=100)
    password = models.CharField(max_lenght=32)
    image = models.ImageField(upload_to='profile_images/',blank=True, null=True)

class Task(models.Models):
    task_id = models.CharField(primary_key=True,validators=[MinValueValidator(1)])
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_lenght=256)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)




