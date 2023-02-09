from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    
    # name = forms.CharField(
    #     widget=forms.TextInput(
    #                         attrs={
    #                             'style' : 'width: 150px;',
    #                             'class' : 'input is-small mb-2 mt-1',
                                
    #                         }))
    # location = forms.CharField(
    #     widget=forms.ChoiceField(
    #                         attrs={
    #                             'style' : 'width: 150px;',
    #                             'class' : 'input is-small mb-2 mt-1',
                                
    #                         }))
    # amount = forms.DecimalField(
    #     widget=forms.TextInput(
    #                         attrs={
    #                             'style' : 'width: 50px;',
    #                             'class' : 'input is-small mb-2 mt-1',
                                
    #                         }))
    class Meta:
        model=Expense
        fields = ['name', 'location', 'amount','purchased']
        