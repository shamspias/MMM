from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Expenses, Loans, MoneyManagement
from .forms import ExpensesForm, LoansForm, MoneyManagementForm


class ExpensesListView(ListView, LoginRequiredMixin):
    """
    Show List of all Expanses
    """
    model = Expenses


class ExpensesDetailView(DetailView, LoginRequiredMixin):
    """
    Show A Single Expanses
    """
    model = Expenses


class ExpensesCreate(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    """
    Create an Expanse
    """
    model = Expenses
    form_class = ExpensesForm
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense Added!"


class ExpensesUpdate(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    """
    Update an Expense
    """
    model = Expenses
    form_class = ExpensesForm
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense updated!"


class ExpensesDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    """
    Delete an Expanse
    """
    model = Expenses
    success_url = reverse_lazy('expenses_list')
    success_message = "Expense deleted!"


class LoansListView(ListView, LoginRequiredMixin):
    """
    Show List of all Loans
    """
    model = Loans


class LoansDetailView(DetailView, LoginRequiredMixin):
    """
    Show A Single Loans
    """
    model = Loans


class LoansCreate(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    """
    Create a Loan
    """
    model = Loans
    form_class = LoansForm
    success_url = reverse_lazy('loans_list')
    success_message = "Loan Added!"


class LoansUpdate(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    """
    Update a Loan
    """
    model = Loans
    form_class = LoansForm
    success_url = reverse_lazy('loans_list')
    success_message = "Loan updated!"


class LoansDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    """
    Delete a Loan
    """
    model = Loans
    success_url = reverse_lazy('loans_list')
    success_message = "Loan deleted!"


class MoneyManagementListView(ListView, LoginRequiredMixin):
    """
    Show List of Money Management list
    """
    model = MoneyManagement


class MoneyManagementDetailsView(ListView, LoginRequiredMixin):
    """
    Show List of Money Management Details
    """
    model = MoneyManagement


class MoneyManagementCreateView(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    """
    Create Money Management
    """
    model = MoneyManagement
    form_class = MoneyManagementForm
    success_url = reverse_lazy('mm_list')
    success_message = "MM Added!"


class MoneyManagementUpdateView(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    """
    Update Money Management
    """
    model = MoneyManagement
    form_class = MoneyManagementForm
    success_url = reverse_lazy('mm_list')
    success_message = "MM Updated!"


class MoneyManagementDelete(SuccessMessageMixin, DeleteView, LoginRequiredMixin):
    """
    Delete MoneyManagement
    """
    model = MoneyManagement
    success_url = reverse_lazy('mm_list')
    success_message = "MM deleted!"
