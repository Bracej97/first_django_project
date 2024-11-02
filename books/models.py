from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book (up to 100 characters)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Author's name
    published_date = models.DateField()  # Publication date of the book
    is_available = models.BooleanField(default=True)  # Availability of the book

    def __str__(self):
        return f"{self.title} by {self.author}"

    #def published_in_last_10_years(self):
