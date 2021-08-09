from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector, SearchQuery
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, TemplateView

from shop.core.mixins import AnyGroupRequiredMixin
from shop.products.forms import EditProductForm, CheckoutForm
from shop.products.models import Product
from django.core.exceptions import ObjectDoesNotExist


class AboutUsView(TemplateView):
    template_name = 'about.html'


class ContactUsView(TemplateView):
    template_name = 'contact-us.html'


class ShowProductsListView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 6


class SearchProductView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        products = Product.objects.annotate(search=SearchVector('title'), ).filter(search=SearchQuery(query))

        return products


def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('landing_page')

    context = {
        'product': product
    }

    return render(request, 'shop-detail.html', context)


class CreateProductView(AnyGroupRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'price', 'description', 'image']
    template_name = 'create_product.html'
    success_url = reverse_lazy('all_products')


@login_required()
def update_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details', pk)
    else:
        form = EditProductForm(instance=product)

    context = {
        'form': form
    }

    return render(request, 'update_product.html', context)


class DeleteProductView(AnyGroupRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('all_products')


def cart(request):
    user = request.user.id
    products = Product.objects.filter(user=user)
    products_price = sum([p.price for p in products if not p.is_sold])
    product_price_to_display = f"{products_price:.2f}"
    products_delivery = products_price
    total = f"{products_delivery:.2f}"

    context = {
        'products': products,
        'products_price': product_price_to_display,
        'total': total
    }

    return render(request, 'cart.html', context)


def add_product_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user

    product.user = user
    product.save()

    return redirect('cart')


def remove_product_from_cart(request, pk):
    product = Product.objects.get(pk=pk)

    product.user_id = None
    product.save()

    return redirect('cart')


def check_out(request):
    user = request.user
    products = Product.objects.filter(user_id=request.user.id)
    product_price = sum([p.price for p in products if not p.is_sold])
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            for product in Product.objects.filter(user_id=request.user.id):
                product.is_sold = True
                product.save()
            return redirect('landing_page')
    else:
        form = CheckoutForm()

    context = {
        'profile': request.user,
        'user': user,
        'products': products,
        'product_price': product_price,
        'form': form
    }
    return render(request, 'checkout.html', context)


def show_bought_products(request):
    products = Product.objects.filter(user_id=request.user.id)
    bought_products = []

    for product in products:
        if product.is_sold:
            bought_products.append(product)

    context = {
        'products': bought_products
    }
    return render(request, 'bought_products.html', context)