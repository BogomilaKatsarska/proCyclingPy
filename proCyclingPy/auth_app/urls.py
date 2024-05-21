from django.urls import path

from proCyclingPy.auth_app.views import SignUpView, SignInView, SignOutView, ChangePasswordView, select_role, \
    ProfileDetailView

urlpatterns = (
    path('register/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='sign in'),
    path('logout/', SignOutView.as_view(), name='sign out'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('select-role/', select_role, name='select role'),
    path('profile/details/<int:pk>/', ProfileDetailView.as_view(), name='details profile'),
)