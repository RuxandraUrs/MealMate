from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_name', 'category', 'date']
        widgets = {
            'meal_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ex: your meal name'
            }),
            'category': forms.Select(attrs={
                'class': 'input'
            }),
            'date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
        }
 
