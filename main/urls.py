from django.urls import path
from main.views import GetCurrentUSDApi, GetCurrentUSD

urlpatterns = [
    path('get_current_usd_api/', GetCurrentUSDApi.as_view(), name='current_usd_api'),
    path('get_current_usd/', GetCurrentUSD.as_view(), name='current_usd')
]