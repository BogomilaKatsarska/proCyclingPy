from django.urls import path

from proCyclingPy.common.views import index, JobCreateView, JobListView, JobEditView, TeamListView, about_us, \
    JobDetailsView, add_job_to_favourites

urlpatterns = (
    path('', index, name='index'),
    path('create-job/', JobCreateView.as_view(), name='create job'),
    path('edit-job/', JobEditView.as_view(), name='edit job'),
    path('jobs/', JobListView.as_view(), name='all jobs'),
    path('job-details/<int:pk>/', JobDetailsView.as_view(), name='details job'),
    path('add-to-favourites/<int:pk>/', add_job_to_favourites, name='add job to favourites'),
    path('teams/', TeamListView.as_view(), name='all teams'),
    path('about-us/', about_us, name='about us'),
)