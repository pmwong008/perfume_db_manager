from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfumes
from .forms import DBForm
from django.contrib import messages
from django.db import models


def dbman_index(request):
    selected_brand = request.GET.get('brand')
    sort_order = request.GET.get('sort', 'desc')  # default to ascending

    all_brands = Perfumes.objects.values_list('brand', flat=True).distinct().order_by('brand')

    results = Perfumes.objects.all()

    if selected_brand and selected_brand != 'all':
        results = results.filter(brand=selected_brand)

    if sort_order == 'desc':
        results = results.order_by('-id')
    else:
        results = results.order_by('id')

    return render(request, 'perfume_db_manager/dbman_index.html', {
        'results': results,
        'brands': all_brands,
        'selected_brand': selected_brand or 'all',
        'sort_order': sort_order
    })


def dbman_search(request):
    query = request.GET.get('q')
    results = Perfumes.objects.all()

    if query:
        query_str = str(query).strip()
        results = results.filter(
            models.Q(name__icontains=query_str) |
            models.Q(launch_year__icontains=query_str)
        )

    return render(request, 'perfume_db_manager/dbman_search.html', {'results': results, 'query': query})


def dbman_list(request):
    perfumes = Perfumes.objects.all()
    return render(request, 'perfume_db_manager/dbman_list.html', {'perfumes': perfumes})

def dbman_create(request):
    form = DBForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "New Perfume added to database!")
        return redirect('dbman_index')
    return render(request, 'perfume_db_manager/dbman_form.html', {'form': form})

def dbman_update(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    form = DBForm(request.POST or None, instance=perfume)
    if form.is_valid():
        form.save()
        messages.success(request, "Perfume updated successfully!")
        return redirect('dbman_index')
    return render(request, 'perfume_db_manager/dbman_form.html', {'form': form})

def dbman_delete(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    if request.method == 'POST':
        perfume.delete()
        messages.success(request, f"Deleted '{perfume.name}' successfully.")
        return redirect('dbman_index')
    return render(request, 'perfume_db_manager/dbman_confirm_delete.html', {'perfume': perfume})

def dbman_cancel(request):
    messages.warning(request, "Glad you reconsidered. No changes were made.")
    return redirect('dbman/dbman_list')
