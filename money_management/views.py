from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Expenses, Loans, MoneyManagement
from .forms import ExpensesForm, LoansForm, MoneyManagementForm


class ExpensesListView(ListView):
    """
    Show List of all Expanses
    """
    model = Expenses


class ExpensesDetailView(DetailView):
    """
    Show A Single Expanses
    """
    model = Expenses


class ExpensesCreate(SuccessMessageMixin, CreateView):
    """
    Create an Expanse
    """
    model = Expenses
    form_class = ExpensesForm
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense Added!"


class ExpensesUpdate(SuccessMessageMixin, UpdateView):
    """
    Update an Expense
    """
    model = Expenses
    form_class = ExpensesForm
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense updated!"


class ExpensesDelete(SuccessMessageMixin, DeleteView):
    """
    Delete an Expanse
    """
    model = Expenses
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense deleted!"


class LoansListView(ListView):
    """
    Show List of all Loans
    """
    model = Loans


class LoansDetailView(DetailView):
    """
    Show A Single Loans
    """
    model = Loans


class LoansCreate(SuccessMessageMixin, CreateView):
    """
    Create a Loan
    """
    model = Loans
    form_class = LoansForm
    success_url = reverse_lazy('loans_list')
    success_message = "Loan Added!"


class LoansUpdate(SuccessMessageMixin, UpdateView):
    """
    Update a Loan
    """
    model = Loans
    form_class = LoansForm
    success_url = reverse_lazy('loans_list')
    success_message = "Loan updated!"


class LoansDelete(SuccessMessageMixin, DeleteView):
    """
    Delete a Loan
    """
    model = Loans
    success_url = reverse_lazy('loans_list')
    success_message = "Loan deleted!"
