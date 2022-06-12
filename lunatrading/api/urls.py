from django.urls import path
from .views import StockView

urlpatterns = [
    path('all_stocks/', StockView.as_view())
]
