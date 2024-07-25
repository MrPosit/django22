from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator

class AccountManager(models.Manager):
    def with_balance_above(self, amount):
        return self.filter(balance__gt=amount)

class Account(models.Model):
    number = models.CharField(max_length=19, validators=[MinLengthValidator(16), MaxLengthValidator(16)], verbose_name="Номер счета")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', verbose_name="Владелец счета")
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0, validators=[MinValueValidator(0)], verbose_name="Баланс")
    
    objects = AccountManager()
    
    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name} - {self.number}"
    
    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"
