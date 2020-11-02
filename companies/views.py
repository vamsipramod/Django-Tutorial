# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
# Create your views here.


class StockList(APIView):
    # Lists all stocks
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks,many=True)

        return Response(serializer.data)

    # Create's a Stock
    def post(self):
        pass
