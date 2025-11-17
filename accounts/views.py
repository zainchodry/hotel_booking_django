from django.shortcuts import render, redirect
from . forms import *
from . models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, "Account Were Created Successfully")
            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, "register.html", {"form":form, "profile_form":profile_form})


def logout(request):
    auth_logout(request)
    messages.success(request, "You Logout Successfully")
    return redirect('login')


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})