from django import forms


class WeatherSearchForm(forms.Form):
    city = forms.CharField(max_length=100, label="Linn", widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Sisesta linna nimi',
    }))