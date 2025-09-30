from .models import Meal
from collections import Counter

def suggest_meal(user_id, day_of_week):
    meals = Meal.objects.filter(user_id=user_id)
    if not meals.exists():
        return "Salad"  

    meal_names = [meal.meal_name for meal in meals]

    most_common = Counter(meal_names).most_common(1)

    return most_common[0][0] if most_common else "Salad"
