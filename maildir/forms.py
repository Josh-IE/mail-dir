from django import forms
from .models import users

class ContactForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs.update(
			{'class': 'form-control'})
		self.fields['last_name'].widget.attrs.update(
			{'class': 'form-control'})
		self.fields['email'].widget.attrs.update(
			{'class': 'form-control'})
			
	class Meta:
		model = users
		fields = ('first_name', 'last_name', 'email',)
		
		
		