import django_filters

from .models import Transaction, Wallet


class WalletFilter(django_filters.FilterSet):
    class Meta:
        model = Wallet
        fields = ['label']


class TransactionFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = ['wallet', 'txid']
