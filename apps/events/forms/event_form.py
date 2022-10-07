# New file created 
from django import forms
class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = '__all__' 