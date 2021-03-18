from django.db import models


# Create your models here.


# many to one using foreign key

# Let us assume a scenario where there is one reporter and he writes multiple articles
# many articles are written by single reporter


class Reporter(models.Model):
    reporter_name = models.CharField(max_length=200, null=False, blank=False)

    # str methods
    def __str__(self):
        return self.reporter_name


class Article(models.Model):
    article_name = models.CharField(max_length=500, null=False, blank=False)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    # srt method
    def __str__(self):
        return self.article_name


# One to one relationship

# let us assume example of car and owner
# single car will have single owner


class Owner(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=200)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.name


# The above relation has serious drawback
# A single owner can have multiple cars

# one to many
class Owner1(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car1(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        Owner1,
        on_delete=models.CASCADE,
        related_name="Car",
    )

    def __str__(self):
        return self.name


# Lets have a scenario where a car is driven by driver
# many driver can drive many car


class Driver(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car2(models.Model):
    name = models.CharField(max_length=200)
    driver = models.ManyToManyField(
        Driver,
        related_name="Cars",
    )

    def __str__(self):
        return self.name