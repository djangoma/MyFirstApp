from django import forms

from .models import Journal

class ViewJournalForm(forms.ModelForm):

    class Meta:
        model = Journal
        fields='__all__'
        
class ContactForm(forms.Form):
    name=forms.CharField()
    message=forms.CharField(widget=forms.Textarea)
	
    def send_email(self):
	    pass

class JournalForm(forms.ModelForm):
    class Meta:
	    model=Journal
	    exclude=('empid',)
