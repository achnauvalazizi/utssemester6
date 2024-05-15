from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import User, RekeningBank, Transaksi

class UserList(ListView):
    model = User
    queryset = User.objects.all()

class UserDetail(DetailView):
    model = User

class RekeningBankList(ListView):
    model = RekeningBank
    queryset = RekeningBank.objects.all()

class RekeningBankDetail(DetailView):
    model = RekeningBank

class TransaksiList(ListView):
    model = Transaksi
    queryset = Transaksi.objects.all()

class TransaksiDetail(DetailView):
    model = Transaksi
