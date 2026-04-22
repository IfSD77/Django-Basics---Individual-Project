from django import forms
from .models import Project, ConstructionType


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'construction_type',
            'location',
            'postcode',
            'built_in',
            'contract_value',
            'contract_value_confidential',
            'description',
            'image',
        ]

        labels = {
            'name': 'Project Name',
            'construction_type': 'Construction Type',
            'location': 'Location',
            'postcode': 'Postcode',
            'built_in': 'Built In (Year)',
            'contract_value': 'Contract Value (£)',
            'contract_value_confidential': 'Contract Value is Confidential',
            'description': 'Description',
            'image': 'Main Project Image',
        }

        help_texts = {
            'built_in': 'Year when the project was completed',
            'contract_value': 'Approximate contract value in GBP',
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'postcode': forms.TextInput(attrs={'placeholder': 'e.g. RH1 1AA'}),
            'built_in': forms.NumberInput(attrs={'placeholder': 'e.g. 2023'}),
        }

    def clean_built_in(self):
        built_in = self.cleaned_data.get('built_in')
        if built_in and (built_in < 1900 or built_in > 2026):
            raise forms.ValidationError("Year must be between 1900 and 2026.")
        return built_in

    def clean_contract_value(self):
        value = self.cleaned_data.get('contract_value')
        if value and value < 0:
            raise forms.ValidationError("Contract value cannot be negative.")
        return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['built_in'].widget.attrs['readonly'] = True
            self.fields['built_in'].widget.attrs['disabled'] = True
            self.fields['built_in'].help_text = "Year cannot be changed after creation"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['built_in'].widget.attrs['readonly'] = True
            self.fields['built_in'].widget.attrs['disabled'] = True
            self.fields['built_in'].help_text = "Year cannot be changed after creation"

            self.fields['construction_type'].widget.attrs['readonly'] = True
            self.fields['construction_type'].widget.attrs['disabled'] = True
            self.fields['construction_type'].help_text = "Construction type cannot be changed after creation"