from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = ["ic01", "account_name", "benchmark_date",
                  "profit", "created_at", "updated_at"]