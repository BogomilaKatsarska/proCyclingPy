from django.urls import path

from proCyclingPy.auth_app.views import SignUpView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='sign up'),
    # path('login/'),
    # path('logout/'),
    # path('change-password/'),
    # path('reset-password/'),
)