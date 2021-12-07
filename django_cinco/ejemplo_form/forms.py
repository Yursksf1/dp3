
# Django
from django import forms

from ejemplo_form.models import Tabla_dos, Tabla_uno

class Tabla_dosForm(forms.ModelForm):
    """Tabla_dos model form."""

    class Meta:
        """Form settings."""

        model = Tabla_dos
        fields = ['name', 'referencia']


class Tabla_unoForm(forms.ModelForm):
    """Tabla_uno model form."""

    class Meta:
        """Form settings."""

        model = Tabla_uno
        fields = ['name',]
