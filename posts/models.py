from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries import countries


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    introduction = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


countries_list = []

for code, name in list(countries):
    name_tuple = (name, name)
    countries_list.append(name_tuple)


class Countries(models.Model):
    country = models.CharField(max_length=200, choices=countries_list, null=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = "Countries"


class Activity(models.Model):
    activity = models.CharField(max_length=50)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = "Activities"


class Destination(models.Model):
    destination = models.CharField(max_length=200)

    def __str__(self):
        return self.destination

    class Meta:
        verbose_name_plural = "Destinations"


class Text(models.Model):
    option_key = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Texts"


class CitizenshipCountries(models.Model):
    citizenship_country = models.CharField(max_length=200, choices=countries_list, null=True)
    text = models.TextField()

    def __str__(self):
        return self.citizenship_country

    class Meta:
        verbose_name_plural = "Citizenship countries"
