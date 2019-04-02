from django.db import models

#Модель заказов
class Order(models.Model):
    number = models.CharField(max_length=255)
    created_date = models.DateTimeField('date created')

#Модель товаров
class OrderItems(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField(default=0)
    amount = models.IntegerField(default=1)