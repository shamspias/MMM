from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Expenses, Loans, MoneyManagement
from .forms import ExpensesForm, LoansForm, MoneyManagementForm
