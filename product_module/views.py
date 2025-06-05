from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import Http404
from .models import Product
from .forms import ProductForm
from module_engine.models import Module

def is_manager(user):
    return user.groups.filter(name='manager').exists()

def is_user(user):
    return user.groups.filter(name='user').exists()

def check_module_installed():
    try:
        module = Module.objects.get(name='product_module')
        return module.is_installed
    except Module.DoesNotExist:
        return False

@login_required
def product_list(request):
    if not check_module_installed():
        raise Http404("Module is not installed")
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {'products': products})

@login_required
@user_passes_test(lambda u: is_manager(u) or is_user(u))
def product_create(request):
    if not check_module_installed():
        raise Http404("Module is not installed")
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('product_module:product_list')
    else:
        form = ProductForm()
    return render(request, 'product_module/product_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(lambda u: is_manager(u) or is_user(u))
def product_update(request, pk):
    if not check_module_installed():
        raise Http404("Module is not installed")
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_module:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_module/product_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_manager)
def product_delete(request, pk):
    if not check_module_installed():
        raise Http404("Module is not installed")
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_module:product_list')
    return render(request, 'product_module/product_confirm_delete.html', {'product': product})
