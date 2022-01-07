from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import DweetForm


@login_required
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("social:dashboard")

    followed_dweets = Dweet.objects.filter(
        user__profile__in = request.user.profile.follows.all()
    ).order_by("-data")

    return render(
        request,
        "social/dashboard.html",
        context={"form": form, "dweets": followed_dweets},
    )


@login_required
def profiles(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social/profiles.html", context={"profiles": profiles})


@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":

        current_user_profile = request.user.profile
        data = request.POST

        # ?
        print(data)
        action = data.get("follow")

        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "social/profile.html", context={"profile": profile})