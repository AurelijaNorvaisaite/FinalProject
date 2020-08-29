from dal import autocomplete

from django import forms

from .models import RegistryFilter, Registry


class CostInputForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CostInputForm, self).__init__(*args, **kwargs)
        self.fields['expense_type'].choices = list({(r.expense_type, r.expense_type) for r in Registry.objects.all() if r.active == 'active'})

    expense_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'),
                                   input_formats=('%Y-%m-%d', )
                                   )
    expense_type = forms.ChoiceField()
    expense_supplier = forms.CharField()
    expense_invoice_numb = forms.CharField()
    expense_invoice_total = forms.DecimalField(widget=forms.NumberInput(attrs={'id': 'form_expense_invoice_total', 'step': "0.01"}))

    def clean(self):
        # Data from the form is fetched using super function.
        super(CostInputForm, self).clean()

        # Extract the username and text field from the data.
        suma = self.cleaned_data.get('expense_invoice_total')

        if suma and suma < 0:
            self._errors['expense_invoice_total'] = self.error_class([
                'It has to be possitive'])

        return self.cleaned_data


    class Meta:
        model = RegistryFilter
        fields = ['expense_date', 'expense_type', 'expense_supplier', 'expense_invoice_numb', 'expense_invoice_total']
        widgets = {
            'expense_supplier': autocomplete.ModelSelect2(url='expense_supplier-autocomplete')
        }


class CostTypeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['active'].initial = 'active'

    expense_type = forms.CharField(label='Pavadinimas')
    ACTIVE_CHOICES = [('active', 'active'),
                     ('not_active', 'notactive')]
    active = forms.ChoiceField(label='Aktyvus', choices=ACTIVE_CHOICES)


    class Meta:
        model = Registry
        fields = ['expense_type', 'active']


class EditingForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        super(EditingForm, self).save(*args, **kwargs)
        return self

    class Meta:
        model = Registry
        fields = ('expense_type', 'active')
        labels = {
            "expense_type": "Pavadinimas",
            'active': "Aktyvus"
        }

