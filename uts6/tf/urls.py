from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('rekeningbang/', views.RekeningBankList.as_view(), name='rekeningbank-list'),
    path('rekeningbank/<int:pk>/', views.RekeningBankDetail.as_view(), name='rekeningbank-detail'),
    path('transaksi/', views.TransaksiList.as_view(), name='transaksi-list'),
    path('transaksi/<int:pk>/', views.TransaksiDetail.as_view(), name='transaksi-detail'),
]
