from rest_framework import serializers
from .models import User, RekeningBank, Transaksi

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id_pengguna', 'nama_pengguna', 'email', 'saldo')
  # Tidak menyertakan password di serializer untuk keamanan

class RekeningBankSerializer(serializers.ModelSerializer):
  class Meta:
    model = RekeningBank
    fields = ('id_rekening', 'nama_bank', 'nomor_rekening')
  # Tidak menampilkan id_pengguna untuk keamanan

class TransaksiSerializer(serializers.ModelSerializer):
  id_pengirim_nama = serializers.CharField(source='id_pengirim.nama_pengguna', read_only=True)
  id_penerima_nama = serializers.CharField(source='id_penerima.nama_pengguna', read_only=True)
  class Meta:
    model = Transaksi
    fields = ('id_transaksi', 'id_pengirim', 'id_pengirim_nama', 'id_penerima', 'id_penerima_nama', 'jumlah_transfer', 'tanggal_transaksi')

class UserTransactionSerializer(serializers.ModelSerializer):
  transaksi = TransaksiSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = ('id_pengguna', 'nama_pengguna', 'email', 'saldo', 'transaksi')

