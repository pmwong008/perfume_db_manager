from django import forms
from .models import Perfumes

'''
class DBForm(forms.ModelForm):
    class Meta:
        model = Perfumes
        fields = '__all__'
'''
class DBForm(forms.ModelForm):
    class Meta:
        model = Perfumes
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'launch_year': forms.TextInput(attrs={'class': 'small-input'}),
            'main_accords': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'longevity': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'sillage': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

    def clean_main_accords(self):
        data = self.cleaned_data['main_accords']
        if isinstance(data, str):
            import json
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                raise forms.ValidationError("Please enter valid JSON (e.g. [\"floral\", \"woody\"])")
        return data
