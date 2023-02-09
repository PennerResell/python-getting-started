from django import forms
from .models import Expense
from bootstrap_datepicker_plus.widgets import DatePickerInput

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields = ['name', 'location', 'amount','purchased']
        widgets = {
            'purchased': DatePickerInput
        }
        