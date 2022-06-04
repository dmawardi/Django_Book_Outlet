from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return f"({self.code}){self.name}"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"{self.street}, {self.city}. {self.postal_code}"

    # Fixes the default Django behavior of adding an additional
    # s to pluralize address
    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # One-to-one relationship
    # does not require using _set as it's not one to manyz
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    # Return full name

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # Replace default output
    def __str__(self) -> str:
        return self.full_name()
        # return super().__str__()


class Book(models.Model):
    title = models.CharField(max_length=50)
    # rating is between 1-5
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # on_delete options:
    # Cascade - Delete all books if author is deleted
    # set null - set to null if author deleted
    # related name will allow a command to return all books on Author object
    # this is more convenient than using book_set (one to many rel)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")

    is_bestselling = models.BooleanField(default=False)
    # By setting blank to true, the admin panel also no longer requires it for form input
    # editable=false has the same effect but also removes it from the admin form
    slug = models.SlugField(default="", null=False, db_index=True)

    # Many to many relationship
    # on delete is not useable here
    # related name is for inverse relationship
    published_countries = models.ManyToManyField(
        Country, related_name="books")

    # These functions are a part of the Model class
    # Allows us to override default save
    def save(self, *args, **kwargs):
        # Create slug before save using title
        self.slug = slugify(self.title)
        # Init super class and save using default save function
        super().save(*args, **kwargs)

    # Allows an absolute url to be used in django html without using url block
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # Allows you to customize the return string when querying the models using shell

    def __str__(self) -> str:
        return f"{self.title} (Rating:{self.rating})"
        # return super().__str__()
