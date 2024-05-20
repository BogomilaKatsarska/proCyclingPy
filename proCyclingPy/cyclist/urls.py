from django.urls import path

from proCyclingPy.cyclist.views import EditCyclist, CyclistListView

urlpatterns = (
    path('edit/<int:pk>/', EditCyclist.as_view(), name='edit cyclist'),
    path('all/', CyclistListView.as_view(), name='all cyclists'),
)