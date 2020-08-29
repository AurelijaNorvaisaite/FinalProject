from django.db import models


class Registry(models.Model):
    expense_type = models.CharField(max_length=25)
    ACTIVE_CHOICES = [('active', 'active'),
                      ('not_active', 'not active')]
    active = models.CharField(max_length=25, choices=ACTIVE_CHOICES)

    def __str__(self):
        return self.expense_type


class RegistryFilter(models.Model):
    expense_date = models.DateField()
    expense_type = models.CharField(max_length=25)
    expense_supplier = models.CharField(max_length=25)
    expense_invoice_numb = models.CharField(max_length=25)
    expense_invoice_total = models.FloatField()

    def __str__(self):
        return self.expense_supplier

    class Meta:
        ordering = ['expense_date']



