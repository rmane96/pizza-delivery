from unittest.util import _MAX_LENGTH
from orders.models import Order
from rest_framework import serializers, generics

class OrderCreateSerializer(serializers.ModelSerializer):
    
    
    SIZES = (
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA_LARGE','extralarge')
    )
    
    ORDER_STATUS = (
        ('PENDING','pending'),
        ('IN_TRANSIT','intransit'),
        ('DELIVERED','delivered'),
        ('CANCELLED','cancelled')
    )
    
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()
    username = serializers.CharField(source='customer.username',read_only=True)
    
    class Meta:
        model = Order
        fields = ['username','id','customer','size','order_status','quantity']
    
class OrderDetailSerializer(serializers.ModelSerializer):
    
    size = serializers.CharField(max_length=20)
    order_status=serializers.CharField(default='PENDING')
    quantity=serializers.IntegerField()
    username = serializers.CharField(source='customer.username',read_only=True)

    
    
    class Meta:
        model=Order
        fields=['username','id','size','order_status','quantity','created','updated']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    
    order_status = serializers.CharField(default='PENDING')

    class Meta:
        model=Order
        fields = ['order_status']