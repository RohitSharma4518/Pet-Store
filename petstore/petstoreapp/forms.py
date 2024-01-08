from petstoreapp.models import Pet
from django.forms import ModelForm


class RegisterNewPet(ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"
