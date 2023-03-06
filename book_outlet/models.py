from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# After you create the models, execute the following commands:
# python3 manage.py makemigrations (Creates the SQL code to get ready the BBDD. We can see it on the migrations folder)
# python3 manage.py migrate (Executes the SQL code)

# There is a Many to Many Relationship between Countries and Books
# In order to add data MM we will need to use the add() method
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)


# There is a One to One Relationship between Address and Author
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


# There is a One to Many Relationship between Authors and Books
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        # return f"{self.first_name} {self.last_name}"
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=70)  # More information in Django Model Field Reference
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True
                               , related_name="books")  # Deletes any related Book from an author
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)  # harry-potter-1
    published_countries = models.ManyToManyField(Country, null=False, related_name="books")

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    """ #We control the slug field in the administration form (see admin.py)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)     #Transforms the title tag into a slug tag format
        super().save(*args, **kwargs)
    """

    def __str__(self):
        return f"{self.title} ({self.rating})"
