from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2', 'role']

        #TODO check super().__init__
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #TODO: check below
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields['email'].widgets.attrs.update({
            'placeholder': 'Enter your e-mail'
        })

        self.fields['password1'].widgets.attrs.update({
            'placeholder': 'Enter your password'
        })

        self.fields['password2'].widgets.attrs.update({
            'placeholder': 'Enter your password'
        })
        #
        # self.fields['role'].label = 'Profile Type'