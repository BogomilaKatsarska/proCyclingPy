from django.shortcuts import render

from proCyclingPy.cyclist.models import Cyclist


def calories(request):
    user_pk = request.user.pk
    logged_cyclist = Cyclist.objects.get(pk=user_pk)

    context = {
        'user': logged_cyclist,
        'daily_kcal_loose_weight': logged_cyclist.daily_kcal_loose_weight,
        'daily_kcal_maintain_weight': logged_cyclist.daily_kcal_maintain_weight,
    }
    return render(request, 'calories/calories.html', context)