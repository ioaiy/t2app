from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .filters import TransactionFilter, WalletFilter
from .models import Transaction, Wallet
from .serializers import TransactionSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WalletFilter
    ordering_fields = ['label', 'balance']
    ordering = ['label']


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TransactionFilter
    ordering_fields = ['wallet_id', 'txid', 'amount']
    ordering = ['wallet_id']