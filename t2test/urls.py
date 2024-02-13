from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('t2test.apps.ledgers.urls', namespace='ledgers')),
    path('admin/', admin.site.urls),
]
