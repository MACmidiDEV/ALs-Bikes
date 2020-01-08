from django import forms
from .models import Bike


class BikePostForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = ('name', 'description', 'image', 'price', 'tag', 'published_date')