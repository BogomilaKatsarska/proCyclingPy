# import requests
from django.shortcuts import render

from proCyclingPy.cyclist.models import Cyclist


def calories(request):
    # food_result = requests.get('https://api.edamam.com/api/food-database/v2/parser?app_id=e4de3ea6&app_key=df551ee705ee3f4534e7c14576c41fb0&ingr=')

    user_pk = request.user.pk
    logged_cyclist = Cyclist.objects.get(pk=user_pk)

    context = {
        'user': logged_cyclist,
        'daily_kcal_loose_weight': logged_cyclist.daily_kcal_loose_weight,
        'daily_kcal_maintain_weight': logged_cyclist.daily_kcal_maintain_weight,
    }
    return render(request, 'calories/calories.html', context)