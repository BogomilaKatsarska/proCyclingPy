from django.urls import path

from proCyclingPy.cyclist.views import EditCyclist

urlpatterns = (
    path('edit/<int:pk>/', EditCyclist.as_view(), name='edit cyclist'),
)