from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)   # harry-potter-1

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    """ #We control the slug field in the administration form (see admin.py)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)     #Transforms the title tag into a slug tag format
        super().save(*args, **kwargs)
    """

    def __str__(self):
        return f"{self.title} ({self.rating})"