from django import forms

class BusquedaForm(forms.Form):
    busqueda = forms.CharField(
        max_length=200,
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Buscar'})
    )

