from animal.models import Animal
from django.forms import ModelForm


class FotoAnimalForm(ModelForm):
	class Meta:
		model = Animal
		fields = ['foto']
		labels = {
			'foto': '',
		}