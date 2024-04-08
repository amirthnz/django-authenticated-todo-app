from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import ChangePasswordForm, UserLoginForm, SetNewPasswordForm, SetNewPasswordForm

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('login/', auth_views.LoginView.as_view(form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Password reset using django classes form_class=forms.PassResetForm
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=SetNewPasswordForm),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(form_class=SetNewPasswordForm),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # User Dashboard
    path('password-change/', auth_views.PasswordChangeView.as_view(form_class=ChangePasswordForm),
         name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile-edit/', views.profile_update, name='profile_update'),
    path('dashboard/', views.AccountDashboard, name='dashboard'),
]