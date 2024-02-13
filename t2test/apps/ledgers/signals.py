from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Transaction


@receiver(post_save, sender=Transaction)
def update_wallet_balance(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            wallet = instance.wallet
            wallet.balance -= instance.amount  # Предполагается, что amount может быть отрицательным для списания
            wallet.save()
