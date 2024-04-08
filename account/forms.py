from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, PasswordResetForm, \
    SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Repeat Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}, ))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    twitter = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        gender_choices = (('Male', 'Male'), ('Female', 'Female'))
        model = Profile
        fields = ('profile_picture', 'bio', 'facebook', 'twitter', 'instagram', 'gender', 'date_of_birth')
        widgets = {
            'gender': forms.Select(choices=gender_choices, attrs={'class': 'form-control'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
