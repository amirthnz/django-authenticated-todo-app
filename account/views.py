from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from tasks.models import Task


# Create your views here.
class AccountLogin(auth_views.LoginView):
    # form_class =
    template_name = "registration/login.html"


@login_required
def AccountDashboard(request):
    tasks = Task.objects.filter(user=request.user)
    tasks_done = tasks.filter(done=True)
    tasks_activity = ((tasks_done.count() / tasks.count())*100)

    tasks_activity = int(tasks_activity)
    task_level = tasks_activity / 20
    task_level = int(task_level)
    print(task_level)
    my_num = [1, 2, 3, 4, 5]
    context = {
        'tasks': tasks,
        'tasks_done': tasks_done,
        'tasks_activity': tasks_activity,
        'task_level': task_level,
        'my_num': my_num,
    }

    return render(request, 'account/dashboard.html', context)


def account_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            profile = Profile.objects.create(user=new_user)
            profile.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'account/register.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request, 'account/profile_update.html', context)