from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import User, RekeningBang, Transaksi

class UserList(ListView):
    model = User
    queryset = User.objects.all()

class UserDetail(DetailView):
    model = User

class RekeningBangList(ListView):
    model = RekeningBank
    queryset = RekeningBang.objects.all()

class RekeningBangDetail(DetailView):
    model = RekeningBank

class TransaksiList(ListView):
    model = Transaksi
    queryset = Transaksi.objects.all()

class TransaksiDetail(DetailView):
    model = Transaksi
