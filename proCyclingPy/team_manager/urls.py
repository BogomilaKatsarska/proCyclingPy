from django.urls import path

from proCyclingPy.team_manager.views import EditTeamManager

urlpatterns = (
    path('edit/<int:pk>/', EditTeamManager.as_view(), name='edit team manager'),
)

