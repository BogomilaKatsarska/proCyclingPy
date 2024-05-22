from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from proCyclingPy.common.forms import JobCreateForm, JobEditForm
from proCyclingPy.common.models import Job, Team, FavouriteJob
from proCyclingPy.cyclist.models import Cyclist
from proCyclingPy.team_manager.models import TeamManager


def index(request):
    recently_added_jobs = Job.objects.order_by('-created_at')[:3]
    top_three_cyclists = Cyclist.objects.order_by('-points')[:3]
    context = {
        'recently_added_jobs': recently_added_jobs,
        'top_three_cyclists': top_three_cyclists,
    }
    return render(request, 'common/index.html', context)


def about_us(request):
    return render(request, 'common/about-us.html')


class JobCreateView(CreateView):
    template_name = 'common/create-job.html'
    form_class = JobCreateForm
    extra_context = {'title': 'Add New Job'}
    success_url = reverse_lazy('all jobs')

    def form_valid(self, form):
        user_pk = self.request.user
        team_manager = TeamManager.objects.get(pk=user_pk)
        form.instance.team_manager = team_manager
        return super(JobCreateView, self).form_valid(form)


class JobDetailsView(DetailView):
    model = Job
    template_name = 'common/details-job.html'


class JobEditView(UpdateView):
    model = Job
    form_class = JobEditForm
    template_name = 'common/edit-job.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        job_obj = self.get_object()
        user_obj = self.request.user
        if job_obj.team_manager == user_obj:
            return True
        return False


class JobListView(ListView):
    template_name = 'common/jobs.html'
    model = Job
    extra_context = {
        'all_jobs': Job.objects.all(),
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_anonymous:
            return context
        context['fav_jobs'] = FavouriteJob.objects.filter(user=self.request.user)

        return context

    #TODO: check below
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')

        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(title__icontains=pattern.lower())
        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


class TeamListView(ListView):
    template_name = 'common/teams.html'
    model = Team
    extra_context = {
        'all_teams': Team.objects.all(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('name')

        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(name__icontains=pattern.lower())
        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


def add_job_to_favourites(request, pk):
    user_pk = request.user.pk
    if not Cyclist.objects.filter(pk=user_pk).exists():
        return redirect('index')

    job = get_object_or_404(Job, pk=pk)

    if not FavouriteJob.objects.filter(user=request.user, job=job).exists():
        FavouriteJob.objects.create(
            user=request.user,
            job=job,
        )

    return redirect('all jobs')