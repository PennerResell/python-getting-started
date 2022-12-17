from django.shortcuts import render, get_object_or_404
from .models import Expense


def expense_list(request):
    expenses = Expense.purchased.all()
    return render(request,
                 'penner/expense/list.html',
                 {'expenses': expenses})


def expense_detail(request, id):
    expense = get_object_or_404(Expense,
                             id=id)
    return render(request,
                  'penner/expense/detail.html',
                  {'expense': expense})