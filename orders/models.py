from django.db import models
from authentication.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


class Order(models.Model):
    
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
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=20,
        null=False,
        choices=SIZES,
        default = SIZES[0][0]
        )
    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default=ORDER_STATUS[0][0])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(100)])
    
    def __str__(self) -> str:
        return f'{self.customer} - {self.size}'