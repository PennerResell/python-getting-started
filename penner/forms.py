from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    purchased = forms.DateField(widget=forms.TextInput(attrs= {
      'class':'datepicker'
    }))
    class Meta:
        model=Expense
        fields = ['location', 'name', 'amount','purchased']
        
        