from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    base_price = models.DecimalField(max_digits=15, decimal_places=2)
    use_bank = models.BooleanField(default=False)
    loan = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

class Service(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=15, decimal_places=2)