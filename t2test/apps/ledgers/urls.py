from django.urls import include, path
from rest_framework import routers
from t2test.apps.ledgers.views import TransactionViewSet, WalletViewSet

app_name = 'ledgers'

router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
