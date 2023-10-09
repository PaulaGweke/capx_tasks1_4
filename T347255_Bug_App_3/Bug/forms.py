from django import forms
from .models import Bug

class BugRegistrationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'bug_type', 'status', 'report_date']
