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
    CHOICE_MONTH = (
        ('January', 'Jan'),
        ('February', 'Feb'),
        ('March', 'Mar'),
        ('April', 'Apr'),
        ('May', 'May'),
        ('June', 'Jun'),
        ('July', 'Jul'),
        ('August', 'Aug'),
        ('September', 'Sep'),
        ('October', 'Oct'),
        ('November', 'Nov'),
        ('December', 'Dec'),

    )
    salary = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    expense = models.ManyToManyField(Expenses, blank=True, related_name='monthly_expense')
    loan = models.ManyToManyField(Loans, blank=True, related_name='loan')
    year = models.CharField(max_length=10, blank=True, null=True)
    month = models.CharField(max_length=50, choices=CHOICE_MONTH, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.salary) + " In " + self.month + " Month"
