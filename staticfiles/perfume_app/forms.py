from django import forms
from perfume_db_manager import Perfumes

class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfumes
        fields = '__all__'