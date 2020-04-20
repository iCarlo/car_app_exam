from .models import Cars
from django import forms
from django.forms import Form


class CarsForm(Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Car name...'}))
    color = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Car color...'}))
    picture = forms.FileField(required=True)

    def save(self):
        cleaned_data = self.cleaned_data
        car_entry = Cars.objects.create(
            name=cleaned_data['name'],
            color=cleaned_data['color'],
            picture=cleaned_data['picture']
        )
        car_entry.save()
