from django import forms
from .models import Bike


class BikePostForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = ('title', 'content', 'image', 'tag', 'published_date')