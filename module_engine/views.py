from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .models import Module

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_engine/module_list.html', {'modules': modules})

def install_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if not module.is_installed:
        module.is_installed = True
        module.save()
        messages.success(request, f'Module {module.name} has been installed successfully.')
    return redirect('module_engine:module_list')

def uninstall_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if module.is_installed:
        module.is_installed = False
        module.save()
        messages.success(request, f'Module {module.name} has been uninstalled successfully.')
    return redirect('module_engine:module_list')

def upgrade_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    if module.is_installed:
        # Here you would implement the upgrade logic
        # For example, running migrations
        from django.core.management import call_command
        try:
            call_command('makemigrations', 'product_module')
            call_command('migrate', 'product_module')
            messages.success(request, f'Module {module.name} has been upgraded successfully.')
        except Exception as e:
            messages.error(request, f'Error upgrading module: {str(e)}')
    return redirect('module_engine:module_list')
