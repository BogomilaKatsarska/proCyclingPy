from django import forms

from proCyclingPy.cyclist.models import Cyclist


class CyclistEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True

    class Meta:
        model = Cyclist
        fields = '__all__'