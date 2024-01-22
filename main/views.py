from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main.core.exceptions import InvalidApiKeyException
from main.core.utils import get_usd_price_in_rub


class GetCurrentUSD(View):
    def get(self, request):
        result = get_usd_price_in_rub()
        return render(request, 'current_usd.html',
                      {"exchange_str": result})


class GetCurrentUSDApi(APIView):
    def get(self, request):
        try:
            result = get_usd_price_in_rub()
        except InvalidApiKeyException:
            return Response({'error': 'INTERNAL_SERVER_ERROR'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'result': result})
