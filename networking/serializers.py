from rest_framework import serializers
from .models import Netuser, Deposit, Trade, Order, Withdrawl,Link

class NetuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Netuser
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class WithdrawlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdrawl
        fields = '__all__'
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
