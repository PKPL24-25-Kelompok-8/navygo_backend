from rest_framework import serializers
from .models import Pelanggan, TrNavypay

class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrNavypay
        fields = ['id', 'user_id', 'kategori', 'nominal', 'tanggal_transaksi']
        read_only_fields = ['id', 'tanggal_transaksi']

    def validate(self, data):
        # Pastikan kategori yang dikirimkan adalah top_up
        if data.get('kategori') != 'top_up':
            raise serializers.ValidationError("Kategori harus 'top_up' untuk proses top up.")
        return data

    def create(self, validated_data):
        # Ambil instance pelanggan dari field user_id
        pelanggan = validated_data['user_id']
        nominal = validated_data['nominal']

        # Buat record transaksi top-up
        topup_transaksi = TrNavypay.objects.create(**validated_data)
        # Update saldo pelanggan sesuai nominal topup
        pelanggan.saldo_navygo += nominal
        pelanggan.save()
        return topup_transaksi