from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# After you create the models, execute the following commands:
# python3 manage.py makemigrations (Creates the SQL code to get ready the BBDD. We can see it on the migrations folder)
# python3 manage.py migrate (Executes the SQL code)


class Book(models.Model):
    title = models.CharField(max_length=70)  # More information in Django Model Field Reference
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"