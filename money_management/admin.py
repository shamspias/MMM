from django.contrib import admin

from .models import Expenses, Loans, MoneyManagement

# Register your models here.


admin.site.register(Expenses)
admin.site.register(Loans)
admin.site.register(MoneyManagement)
