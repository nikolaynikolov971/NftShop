from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from shop.products.models import Product
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


class ShowAllProfiles(ListView):
    model = Profile
    template_name = 'profiles.html'
    context_object_name = 'profiles'
    paginate_by = 12


@login_required
def profile_to_show(request, pk):
    profile = Profile.objects.get(pk=pk)
    products = Product.objects.all()
    needed_products = [p for p in products if  p.is_sold]

    context = {
        'profile': profile,
        'needed_products': needed_products
    }
    return render(request, 'profiles_details.html', context)
