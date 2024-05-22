from django.urls import path

from proCyclingPy.team_manager.views import EditTeamManager, ViewTeamManagerView

urlpatterns = (
    path('edit/<int:pk>/', EditTeamManager.as_view(), name='edit team manager'),
    path('details/<int:pk>/', ViewTeamManagerView.as_view(), name='details team manager'),
    # path('delete/<int:pk>/', DeleteCyclistView.as_view(), name='delete cyclist'),
)

