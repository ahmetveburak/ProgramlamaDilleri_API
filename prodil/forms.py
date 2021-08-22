from django import forms

from .models import Resource


class ResourceEditForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = "__all__"
