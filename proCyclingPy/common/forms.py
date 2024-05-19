from django import forms

from proCyclingPy.common.models import Job


class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('team_manager',)


class JobEditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team_manager'].disabled = True
