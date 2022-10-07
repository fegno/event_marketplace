# New file created 
from django import forms
class DestinationForm(forms.ModelForm):
	class Meta:
		model = Destination
		fields = '__all__' 