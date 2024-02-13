from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=20, decimal_places=18, default=0)

class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=20, decimal_places=18)

    class Meta:
        unique_together = [['wallet', 'txid']]