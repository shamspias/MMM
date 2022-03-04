from django import forms

from .models import Expenses, Loans, MoneyManagement


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses


class LoansForm(forms.ModelForm):
    class Meta:
        model = Loans


class MoneyManagementForm(forms.ModelForm):
    class Meta:
        model = MoneyManagement
