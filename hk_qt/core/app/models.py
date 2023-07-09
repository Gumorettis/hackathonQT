from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    income = models.IntegerField()


class Loan(models.Model):
    value = models.IntegerField(default=None, null=True)
    start = models.DateField()
    end = models.DateField()
    status = models.CharField(max_length=15, default="")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="loans")
