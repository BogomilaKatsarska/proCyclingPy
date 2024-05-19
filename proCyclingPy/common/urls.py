from django.urls import path

from proCyclingPy.common.views import index, JobCreateView, JobListView, JobEditView, TeamListView

urlpatterns = (
    path('', index, name='index'),
    path('create-job/', JobCreateView.as_view(), name='create job'),
    path('edit-job/', JobEditView.as_view(), name='edit job'),
    path('jobs/', JobListView.as_view(), name='all jobs'),
    path('teams/', TeamListView.as_view(), name='all teams'),
)