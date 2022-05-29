from django.forms import ModelForm, EmailInput

from persona.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'gmail': EmailInput(attrs={'type': 'email'})
        }