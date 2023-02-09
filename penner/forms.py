from django import forms
from .models import Expense

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ExpenseForm(forms.ModelForm):
    purchased = forms.DateField(widget=DateInput)
    class Meta:
        model=Expense
        fields = ['location', 'name', 'amount','purchased']
        
        