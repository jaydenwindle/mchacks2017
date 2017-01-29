from django import forms

from .models import WorkEntry, EducationEntry, ProjectEntry

class WorkEntryForm(forms.ModelForm):
    class Meta:
        model = WorkEntry 
        fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(WorkEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'startDate':
                self.fields[field_name].label = "Start Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            if field_name == 'endDate':
                self.fields[field_name].label = "End Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            field.widget.attrs['class'] = 'form-control'

class EducationEntryForm(forms.ModelForm):
    class Meta:
        model = EducationEntry 
        fields = ['institution','area','studyType', 'startDate', 'endDate', 'skills','gpa']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(EducationEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProjectEntryForm(forms.ModelForm):
    class Meta:
        model = ProjectEntry 
        fields = ['name', 'gh_repo', 'website', 'description', 'stars', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(WorkEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
