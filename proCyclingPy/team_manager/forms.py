from django import forms

from proCyclingPy.team_manager.models import TeamManager


class TeamManagerEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = TeamManager
        fields = '__all__'


class TeamManagerViewForm(forms.ModelForm):
    class Meta:
        model = TeamManager
        fields = '__all__'