# New file created 
from django import forms
class VenueForm(forms.ModelForm):
	class Meta:
		model = Venue
		fields = '__all__' 