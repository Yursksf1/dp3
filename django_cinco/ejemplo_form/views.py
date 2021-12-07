from django.shortcuts import render
from ejemplo_form.models import Tabla_dos, Tabla_uno
from ejemplo_form.forms import Tabla_dosForm, Tabla_unoForm
import json
# Create your views here.

# SHEEPS
# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from django.http import JsonResponse


class SheepsFeedView(ListView):
    """Return all published sheeps."""

    template_name = 'sheep_list.html'
    model = Tabla_dos
    paginate_by = 200
    context_object_name = 't2'

    def get_queryset(self):
        """Filter by price if it is provided in GET parameters"""
        queryset = super().get_queryset()
        return queryset


class Tabla_dosView(DetailView):
    """Return sheep detail."""

    template_name = 'tabla_dos_detail.html'
    queryset = Tabla_dos.objects.all()
    context_object_name = 't2'


class CreateTabla_dosView(CreateView):
    """Create a new sheep."""

    template_name = 'tabla_dos_form.html'
    form_class = Tabla_dosForm
    success_url = reverse_lazy('app:create')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user
        return context


class CreateTabla_unoView(CreateView):
    """Create a new sheep."""

    template_name = 'tabla_uno_form.html'
    form_class = Tabla_unoForm
    success_url = reverse_lazy('app:create-uno')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user
        return context


def create_table_uno(request):
    print('method', request.method)
    data = {}
    if request.method == 'POST':
        print('es un  llamado post y vamos a guardar ')
        payload = json.loads(request.body)
        name = payload.get('name')
        data = {
            'name': name,
        }
        t = Tabla_uno.objects.create(**data)

        data = {
            'id': t.id,
            'name': t.name
        }

    # just return a JsonResponse
    return JsonResponse(data)


