from django.urls import path

from proCyclingPy.team_manager.views import EditTeamManager, ViewTeamManagerView, DeleteTeamManager

urlpatterns = (
    path('edit/<int:pk>/', EditTeamManager.as_view(), name='edit team manager'),
    path('details/<int:pk>/', ViewTeamManagerView.as_view(), name='details team manager'),
    path('delete/<int:pk>/', DeleteTeamManager.as_view(), name='delete team manager'),
)

