from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Update(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=False)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='users',
    )

    def __str__(self) -> str:
        return self.title


class TimeZone(models.Model):
    timezone_name = models.CharField(max_length=50)
    timezone_delta = models.FloatField(null=False, unique=True)

    def __str__(self) -> str:
        return self.timezone_name


class City(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    on_main = models.BooleanField()
    timezone = models.ForeignKey(
        TimeZone,
        null=True,
        on_delete=models.SET_NULL,
        related_name='timezones',
    )

    class Mets:
        ...

    def __str__(self) -> str:
        return self.name
