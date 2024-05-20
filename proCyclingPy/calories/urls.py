from django.urls import path

from proCyclingPy.calories.views import calories

urlpatterns = (
    path('', calories, name='calories'),
)