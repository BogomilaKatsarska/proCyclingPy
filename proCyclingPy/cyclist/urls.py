from django.urls import path

from proCyclingPy.cyclist.views import EditCyclistView, CyclistListView, ViewCyclistView

urlpatterns = (
    path('edit/<int:pk>/', EditCyclistView.as_view(), name='edit cyclist'),
    path('details/<int:pk>/', ViewCyclistView.as_view(), name='details cyclist'),
    path('all/', CyclistListView.as_view(), name='all cyclists'),
)