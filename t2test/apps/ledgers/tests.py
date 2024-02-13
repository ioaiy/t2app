from decimal import Decimal

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Transaction, Wallet


class WalletViewSetTestCase(APITestCase):
    def setUp(self):
        Wallet.objects.all().delete()  # Очистка предыдущих данных
        # Создание тестовых данных
        Wallet.objects.create(label='Test Wallet 1', balance=Decimal('10.000000000000000000'))
        Wallet.objects.create(label='Test Wallet 2', balance=Decimal('20.000000000000000000'))

    def test_get_wallets(self):
        url = reverse('ledgers:wallet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Исправлено: Учитываем пагинацию или другие факторы, если они применимы
        self.assertEqual(len(response.data['results']), 2)  # Предполагая, что используется пагинация

    def test_create_wallet(self):
        url = reverse('ledgers:wallet-list')
        data = {'label': 'New Wallet', 'balance': '30.000000000000000000'}  # Отправляем как строку
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wallet.objects.count(), 3)
        # Исправлено: Получение кошелька по label, так как id может изменяться
        new_wallet = Wallet.objects.get(label='New Wallet')
        self.assertEqual(new_wallet.balance, Decimal('30.000000000000000000'))

class TransactionViewSetTestCase(APITestCase):
    def setUp(self):
        Transaction.objects.all().delete()  # Очистка предыдущих данных
        self.wallet = Wallet.objects.create(label='Test Wallet', balance=Decimal('15.000000000000000000'))
        # Создаем тестовую транзакцию с корректным Decimal значением
        self.transaction = Transaction.objects.create(wallet=self.wallet, txid='tx123', amount=Decimal('5.000000000000000000'))

    def test_get_transactions(self):
        url = reverse('ledgers:transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Исправлено: Учитываем пагинацию или другие факторы, если они применимы
        self.assertEqual(len(response.data['results']), 1)  # Предполагая, что используется пагинация

    def test_create_transaction(self):
        url = reverse('ledgers:transaction-list')
        data = {'wallet': self.wallet.id, 'txid': 'tx456',
                'amount': '5.000000000000000000'}  # Указываем Decimal для значения amount
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)  # Убедитесь, что количество транзакций увеличилось
        new_transaction = Transaction.objects.get(txid='tx456')
        self.assertEqual(new_transaction.amount, Decimal('5.000000000000000000'))  # Проверка созданной транзакции
        # Проверяем обновление баланса кошелька
        self.wallet.refresh_from_db()
        self.assertEqual(self.wallet.balance, Decimal('5.000000000000000000'))
