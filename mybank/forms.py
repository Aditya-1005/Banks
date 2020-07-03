from django import forms
from .models import Banks, Branches


class BankForm(forms.ModelForm):

    class Meta:
        model = Banks
        fields = ['ID', 'Name']


class BranchForm(forms.ModelForm):

    class Meta:
        model = Branches
        fields = ['Bank_ID', 'IFSC', 'Branch', 'Address', 'City', 'District', 'State']


