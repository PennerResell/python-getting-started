from django.urls import path
from .views import (
    expense_list_veiw,
    expense_detail_veiw,
    expense_create_veiw,
    expense_update_veiw
    )

app_name = 'penner'

urlpatterns = [
    path('', expense_list_veiw, name='list'),
    path('create/', expense_create_veiw, name='create'),
    path('<int:id>/edit/', expense_update_veiw, name='update'),
    path('<int:id>/', expense_detail_veiw, name='detail'),
]
