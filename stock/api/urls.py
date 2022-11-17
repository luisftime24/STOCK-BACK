from django.urls import path
from . import views

urlpatterns = [
    path('stocks', views.get_stocks),
    path('stock/<str:symbol>', views.get_stocks_by_symbol),
]
