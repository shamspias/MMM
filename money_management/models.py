from django.db import models


class Expenses(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Loans(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    loan_from = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class MoneyManagement(models.Model):
    salary = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE, blank=True, null=True)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.salary
