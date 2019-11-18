from django.db import models

# Create your models here.
class Users(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=100)
    balance = models.FloatField(default=0)
    account_type = models.CharField(max_length=10)

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_source = models.CharField(max_length=10)
    transaction_dest = models.CharField(max_length=10)
    