from django.urls import path
from . import views

app_name = 'penner'

urlpatterns = [
    # post views
    path('', views.expense_list, name='expense_list'),
    path('<int:id>/', views.expense_detail, name='expense_detail'),
]
