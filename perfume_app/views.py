from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from perfume_db_manager.models import Perfumes
import json

# Create your views here.
def index(request):
    return render(request,'perfume_app/index.html')

def extract_notes(notes_str):
    notes_set = set()
    try:
        notes_data = json.loads(notes_str)
        if isinstance(notes_data, dict):
            for val in notes_data.values():
                if isinstance(val, list):
                    notes_set.update(str(n) for n in val if n is not None)
                else:
                    if val is not None:
                        notes_set.add(str(val))
        elif isinstance(notes_data, list):
            notes_set.update(str(n) for n in notes_data if n is not None)
        # elif notes_data is not None:
        #     notes_set.add(str(notes_data))
    except Exception:
        if notes_str:
            notes_set.add(str(notes_str))
    return notes_set

def perfumes_list(request):
    all_brands = Perfumes.objects.values_list('brand', flat=True).distinct().order_by('brand')

    notes_set = set()
    for perfume in Perfumes.objects.all():
        if perfume.notes:
            notes_set |= extract_notes(perfume.notes)
    all_notes = sorted(notes_set, key=lambda s: s.lower())

    selected_brands = request.GET.getlist('brand')
    selected_notes = set(request.GET.getlist('note'))
    q = request.GET.get('q', '').strip()

    perfumes_qs = Perfumes.objects.all()

    if selected_brands:
        perfumes_qs = perfumes_qs.filter(brand__in=selected_brands)

    if q:
        tmp_set = set()

        brand_name_results = perfumes_qs.filter(Q(brand__icontains=q) | Q(name__icontains=q))
        for p in brand_name_results:
            tmp_set.add(p)

        for p in perfumes_qs:
            if p.notes:
                perfume_notes = extract_notes(p.notes)
                if any(q.lower() in notes.lower() for notes in perfume_notes):
                    tmp_set.add(p)

        perfumes_qs = list(tmp_set)

    if selected_notes:
        filtered = []
        for p in perfumes_qs:
            if p.notes:
                perfume_notes = extract_notes(p.notes)
                if selected_notes & perfume_notes:
                    filtered.append(p)
        perfumes_qs = filtered

    paginator = Paginator(perfumes_qs, 16)
    page_number = request.GET.get('page') or 1
    perfumes_page = paginator.get_page(page_number)

    no_results = len(perfumes_page) == 0

    return render(request, 'perfume_app/perfumes_list.html', {
        'perfumes': perfumes_page,
        'all_brands': all_brands,
        'all_notes': all_notes,
        'selected_brands': selected_brands,
        'selected_notes': selected_notes,
        'no_results': no_results,
        'q': q,
    })


def perfume_detail(request, pk):
    perfume = Perfumes.objects.get(pk=pk)
    if isinstance(perfume.notes, str):
        try:
            perfume.notes = json.loads(perfume.notes)
        except json.JSONDecodeError:
            perfume.notes = {}
    is_dict = isinstance(perfume.notes, dict)
    context = {
        "perfume": perfume,
        "is_dict": is_dict,
    }
    return render(request, 'perfume_app/perfume_detail.html', context)