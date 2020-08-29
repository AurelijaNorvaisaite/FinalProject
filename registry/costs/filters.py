import django_filters
from django.db.models import Sum
from django_filters.widgets import RangeWidget

from .models import RegistryFilter
from django import forms

# today = datetime.expense_date.today()
# filters = RegistryFilter.objects.filter(date__year=today.year, date__month=today.month)
class RegistryFilterFilter(django_filters.FilterSet):

    # expense_type = django_filters.CharFilter(field_name='expense_type', method='filter_type')
    expense_date = django_filters.DateFilter(label='Datos filtras', widget=forms.DateInput(format='%Y-%m-%d'),
                                     input_formats=('%Y-%m-%d',),
                                     field_name='expense_date')

    expense_date_range = django_filters.DateFromToRangeFilter(label='Datos filtras rėžiais',
                                                        field_name='expense_date',
                                                        widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}))

    expense_type = django_filters.CharFilter(label="Tipo filtras", field_name='expense_type', lookup_expr='icontains')

    def get_labels(self):
        labels = []
        qs = super(RegistryFilterFilter, self).qs
        for registry in qs:
            if registry.expense_type not in labels:
                labels.append(registry.expense_type)
        return labels

    def get_data(self):
        labels = []
        data = []
        qs = super(RegistryFilterFilter, self).qs
        for registry in qs:
            if registry.expense_type not in labels:
                labels.append(registry.expense_type)
                data.append(registry.expense_invoice_total)
            else:
                index = labels.index(registry.expense_type)
                data[index] += registry.expense_invoice_total
        return data

    @property
    def sum(self):
        qs = super(RegistryFilterFilter, self).qs
        return qs.aggregate(Sum('expense_invoice_total'))['expense_invoice_total__sum']


    class Meta:
        model = RegistryFilter
        fields = (
            'expense_date',
            'expense_type'
        )


    # def filter_type(self, queryset, name, expense_type):
    #     return queryset.filter(type__contains=expense_type.split(','))

