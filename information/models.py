from django.db import models


class info(models.Model):
    zid = models.CharField(max_length=5)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    Credit_card_number = models.CharField(max_length=20)
    city = models.CharField(max_length=10)