from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Profile(models.Models):
    user_id = models.IntegerField(validators=[MinValueValidator(1)])
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField(max_lenght=100)
    password = models.CharField(max_lenght=32)
    image = models.ImageField(upload_to='profile_images/',blank=True, null=True)

