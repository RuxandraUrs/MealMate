from django.db import models

from django.db import models

class Meal(models.Model):
    
    user_id = models.IntegerField(default=1)  
    CATEGORY_CHOICES = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snack', 'snack'),
    ]

    meal_name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='lunch'
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.meal_name} ({self.get_category_display()})"
