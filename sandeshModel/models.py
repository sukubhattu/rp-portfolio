from django.db import models
from django.db.models.base import ModelState

# Create your models here.


class Book(models.Model):
    PRINT_TYPE = [
        ("ex", "excellent fine print"),
        ("sn", "student version print"),
        ("eb", "e-book version"),
    ]
    # id is by default primary key
    # we can define our own primary key. But i will use that code using id
    id = models.AutoField(primary_key=True)
    # char field for small text
    name = models.CharField(max_length=200, null=False, blank=False)
    # text field for longer text
    description = models.TextField(blank=True)
    # email filed
    publisher_email = models.EmailField(blank=True)
    # To keep track of original release date
    first_release = models.DateField(auto_now_add=True)
    # To track latest update date
    update_release = models.DateField(auto_now=True)
    # Decimal and float field behaves almost similar in django. so i am using decimal here
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # We have 3 differnet print types
    print_type = models.CharField(max_length=2, choices=PRINT_TYPE, default="ex")
    # lets have boolean field determining if released to the general public or not
    available_to_public = models.BooleanField(default=False)
    # A book db would be awesome if it have a book cover image or some other files for it.
    # I would love to learn it
    # image = models.FilePathField(path="/img")

    # providing some meta data for our books
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "books"

    # Look up with name not with object
    def __str__(self):
        return self.name
