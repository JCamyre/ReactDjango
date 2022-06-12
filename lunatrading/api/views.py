from rest_framework import generics
from django.shortcuts import render
from .serializers import StockSerializer
from .models import Stock


class StockView(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
