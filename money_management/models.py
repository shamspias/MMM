from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    instance_name = instance.name.lower()
    instance_name = instance_name.replace(" ", '-')
    if instance.check_pdf(filename):
        instance_name = 'documents/pdf/' + instance_name
    elif instance.check_doc:
        instance_name = 'documents/word/' + instance_name
    else:
        instance_name = 'user/' + instance_name
    return '{0}'.format(instance_name)


class Document(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    document = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.name

    @staticmethod
    def check_pdf(filename):
        """
        Check the file is pdf or not
        :param filename:
        :return: Boolean
        """
        print('file name', filename)
        if filename.endswith('.pdf'):
            return True
        else:
            return False

    @staticmethod
    def check_doc(filename):
        """
        Check the file is word file or not
        :param filename:
        :return: Boolean
        """

        if filename.endswith('.doc'):
            return True
        elif filename.endswith('.docx'):
            return True
        else:
            return False

    @staticmethod
    def check_image(filename):
        """
        Check the file is image or not
        :param filename:
        :return: Boolean
        """

        if filename.endswith('.png'):
            return True
        elif filename.endswith('.jpg'):
            return True
        elif filename.endswith('.jpeg'):
            return True
        elif filename.endswith('.gif'):
            return True
        elif filename.endswith('.eps'):
            return True
        elif filename.endswith('.tif'):
            return True
        else:
            return False

    @staticmethod
    def check_video(filename):
        """
        Check the file is video or not
        :param filename:
        :return: Boolean
        """
        if filename.endswith('.mp4'):
            return True
        elif filename.endswith('.mov'):
            return True
        elif filename.endswith('.wmv'):
            return True
        elif filename.endswith('.avi'):
            return True
        elif filename.endswith('.mkv'):
            return True
        elif filename.endswith('.mpeg'):
            return True
        elif filename.endswith('.flv'):
            return True
        elif filename.endswith('.swf'):
            return True
        elif filename.endswith('.f4v'):
            return True
        elif filename.endswith('.avchd'):
            return True
        elif filename.endswith('.webm'):
            return True
        elif filename.endswith('.ts'):
            return True

        else:
            return False

    def get_file_size(self):
        """
        Get Document File size
        :return: file size
        """
        if self.document:
            return "0 KB"
        else:
            value = self.document.size
            if value < 512000:
                value = value / 1024.0
                ext = 'KB'
            elif value < 4194304000:
                value = value / 1048576.0
                ext = 'MB'
            else:
                value = value / 1073741824.0
                ext = 'GB'
            return '%s %s' % (str(round(value, 2)), ext)


class Expenses(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    date = models.DateField(auto_now=True)
    additional_files = models.ManyToManyField(Document, blank=True, related_name="expenses")  # Upload multiple files

    def __str__(self):
        return self.name


class Loans(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    loan_from = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(auto_now=True)
    additional_files = models.ManyToManyField(Document, blank=True, related_name="loans")  # Upload multiple files

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
    additional_files = models.ManyToManyField(Document, blank=True,
                                              related_name="money_management")  # Upload multiple files

    def __str__(self):
        return str(self.salary) + " In " + self.month + " Month"

    def get_saving(self):
        """
        Calculate remaining money after expanse
        :return: total remaining money
        """
        total_expense = 0
        for exp in self.expense.all():
            total_expense += exp.amount
        return self.salary - total_expense

    def get_total_expense(self):
        """
        Calculate total expense amount
        :return: total expanse amount
        """
        total_expense = 0
        for exp in self.expense.all():
            total_expense += exp.amount
        return total_expense

    def get_total_loan(self):
        """
        Calculate total amount of loan
        :return:  total loan amount
        """
        total_loan = 0
        for exp in self.loan.all():
            total_loan += exp.amount
        return total_loan
