from django import forms
from houses.models import House


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'square_footage',
            'address',
            'image'
        ]

        labels = {
            'title': 'House title',
            'price': 'price',
            'num_bedrooms': 'Number of Bedrooms',
            'num_bathrooms': 'Number of Bathrooms',
            'square_footage': 'Square footage',
            'address': 'Address' 

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'num_bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'square_footage': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }