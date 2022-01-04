from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "base.html")


def profiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social/profiles.html", context={"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "social/profile.html", context={"profile": profile})