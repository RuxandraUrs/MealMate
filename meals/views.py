from datetime import datetime
from django.shortcuts import render, redirect
from .models import Meal
from .forms import MealForm
from .ai import suggest_meal

def index(request):
    user_id = request.user.id  
    day_of_week = datetime.today().weekday()  
    suggestion = suggest_meal(user_id, day_of_week)
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MealForm()

    meals = Meal.objects.all().order_by('-date')

    return render(request, 'meals/index.html', {
        'form': form,
        'meals': meals,
        'suggestion': suggestion,
    })
