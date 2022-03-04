from django.contrib import admin

from .models import Expenses, Loans, MoneyManagement


# Register your models here.


class MoneyManagementAdmin(admin.ModelAdmin):
    """
    customize Money Management in django default admin
    """
    list_display = ('salary', 'year', 'month', 'get_total_expense', 'get_total_loan', 'get_saving')
    filter_horizontal = ('expense', 'loan')
    fields = ('salary', 'expense', 'loan', 'year', 'month')
    date_hierarchy = 'date'


admin.site.register(Expenses)
admin.site.register(Loans)

admin.site.register(MoneyManagement, MoneyManagementAdmin)
