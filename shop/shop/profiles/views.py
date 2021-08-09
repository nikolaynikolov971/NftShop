from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from shop.profiles.forms import ProfileForm
from shop.profiles.models import Profile


def home_page(request):
    return render(request, 'index.html')


@login_required()
def my_profile(request):
    return render(request, 'my-account.html')


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'update_profile.html', context)