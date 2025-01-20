from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Bill(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill #{self.id}"

class BillDetail(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price
        super().save(*args, **kwargs)
