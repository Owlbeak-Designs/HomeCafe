from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    class DrinkType(models.TextChoices):
        CAPPUCCINO = 'cappuccino', 'Cappuccino'
        LATTE = 'latte', 'Latte'
        FLAT_WHITE = 'flat white', 'Flat White'
        ICED_COFFEE = 'iced coffee', 'Iced Coffee'
        LONG_BLACK = 'long black', 'Long Black'
        ICED_AMERICANO = 'iced americano', 'Iced Americano'

    drink_type = models.CharField(
        max_length = 20,
        choices = DrinkType.choices,
        default = DrinkType.CAPPUCCINO
    )

    ordered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'orders'
    )

    ordered_at = models.DateTimeField(auto_now_add = True)

    claimed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'claimed_orders'
    )

    status = models.CharField(
        max_length = 20,
        choices = [
            ('pending', 'Pending'),
            ('making', 'Making'),
            ('ready', 'Ready')
        ],
        default = 'pending'
    )

    def __str__(self):
        return f"{self.drink_type} (ordered at {self.ordered_at})"