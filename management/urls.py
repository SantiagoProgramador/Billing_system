from django.urls import path
from . import views

urlpatterns = [
    path('billing/', views.billing, name='billing'),
    path('bill/<int:bill_id>/', views.show_bill, name='show_bill'),
]
