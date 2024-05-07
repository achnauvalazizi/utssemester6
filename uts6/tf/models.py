from rest_framework import serializers
from .models import Kategori, Produk

from django.db import models

class User(models.Model):
  id_pengguna = models.AutoField(primary_key=True)
  nama_pengguna = models.CharField(max_length=255, null=False)
  email = models.EmailField(unique=True, null=False)
  password = models.CharField(max_length=255, null=False)
  saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

  def __str__(self):
    return self.nama_pengguna

class RekeningBank(models.Model):
  id_rekening = models.AutoField(primary_key=True)
  id_pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
  nama_bank = models.CharField(max_length=255, null=False)
  nomor_rekening = models.CharField(max_length=255, null=False)

  def __str__(self):
    return f"{self.nama_bank} - {self.nomor_rekening}"

class Transaksi(models.Model):
  id_transaksi = models.AutoField(primary_key=True)
  id_pengirim = models.ForeignKey(User, related_name="transaksi_pengirim", on_delete=models.CASCADE)
  id_penerima = models.ForeignKey(User, related_name="transaksi_penerima", on_delete=models.CASCADE)
  jumlah_transfer = models.DecimalField(max_digits=10, decimal_places=2)
  tanggal_transaksi = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Transfer dari {self.id_pengirim} ke {self.id_penerima} - {self.jumlah_transfer}"
