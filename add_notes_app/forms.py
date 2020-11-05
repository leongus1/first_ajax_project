from django import forms
from .models import Notes
# from django.utils.translation import gettext_lazy as _


class CreateNote(forms.ModelForm):
    class Meta:
        model=Notes
        fields= ['subject']
        labels = {
            'subject': ' '
        }
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder':'Enter Note subject here'})
        }
    def save(self, commit=True):
        title = super(CreateNote, self).save(commit=False)
        title.subject=self.cleaned_data['subject']
        if commit:
            title.save()
        return title
        
        
class AddDescription(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['description']
        widgets = {
            'description': forms.TextInput(attrs={'placeholder':'Enter Note description here'})
        }
        
    def save(self, commit=True):
        desc = super(CreateNote, self).save(commit=False)
        desc.subject=self.cleaned_data['subject']
        if commit:
            desc.save()
        return desc
        
        
