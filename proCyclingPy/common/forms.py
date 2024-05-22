from django import forms

from proCyclingPy.common.models import Job


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('team_manager',)

    # def save(self, commit=True):
    #     job = super().save(commit=commit)
    #     title = self.cleaned_data['title']
    #     specialty = self.cleaned_data['specialty']
    #     salary = self.cleaned_data['salary']
    #     description = self.cleaned_data['description']
    #     job = Job(
    #         team_manager=
    #     )
    #


class JobEditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_manager'].disabled = True
