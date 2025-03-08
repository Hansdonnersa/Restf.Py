# api/urls.py
from django.urls import path
from .views import SumView, AverageView  # Importe suas views aqui

urlpatterns = [
    path('sum/', SumView.as_view(), name='sum'),
    path('average/', AverageView.as_view(), name='average'),
]