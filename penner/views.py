from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Avg, Count, Min, Sum




def expense_list_veiw(request, id=None):
    qs = Expense.objects.all()
    sum = Expense.objects.all().aggregate(Sum('amount'))['amount__sum']
    context = {
        'object_list': qs,
        'sum': sum
        
    }
    return render(request, 'penner/list.html', context)

def expense_detail_veiw(request, id=None):
    obj = get_object_or_404(Expense, id=id)
    context = {
        'object':obj
    }
    return render(request, 'penner/detail.html', context)


def expense_create_veiw(request, id=None):
    form = ExpenseForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=True)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'penner/create-update.html', context)

def expense_update_veiw(request):
    obj = get_object_or_404(Expense, id=id)
    form = ExpenseForm(request.POST or None, instance=obj)
    context = {
        'object':obj,
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=True)
        obj.save()
        context['message'] = 'Information has been saved and updated.'
    return render(request, 'penner/create-update.html', context)