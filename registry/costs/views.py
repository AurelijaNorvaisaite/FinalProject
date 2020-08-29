import datetime
from dal import autocomplete
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from .filters import RegistryFilterFilter
from .models import Registry, RegistryFilter
from .forms import CostInputForm, CostTypeForm, EditingForm


class MainView(TemplateView):
    model = RegistryFilter
    template_name = "main.html"
    context_object_name = 'registry_filters'

    def get(self, request, *args, **kwargs):
        labels = []
        data = []
        today = datetime.date.today()
        filters = RegistryFilter.objects.filter(expense_date__year=today.year, expense_date__month=today.month)

        for registry in filters:
            if registry.expense_type not in labels:
                labels.append(registry.expense_type)
                data.append(registry.expense_invoice_total)
            else:
                index = labels.index(registry.expense_type)
                data[index] += registry.expense_invoice_total

        context = {
            'filters': filters,
            'expense_invoice_total': round(sum([f.expense_invoice_total for f in filters]), 2),
            'labels': labels,
            'data': data
        }
        return render(request, 'main.html', context=context)


class RegistryFilterListView(ListView):
    model = RegistryFilter
    filter_class = RegistryFilterFilter
    template_name = 'registry_input_list.html'
    context_object_name = 'registry_filters'

    def get(self, request, *args, **kwargs):

        filters = RegistryFilter.objects.all()
        f = RegistryFilterFilter(request.GET, queryset=RegistryFilter.objects.all())
        context = {
            'filters': filters,
            'filter': f,
        }

        return render(request, 'registry_input_list.html', context=context)


class RegistryTypeListView(ListView):
    model = Registry
    queryset = Registry.objects.order_by('active', 'expense_type')
    template_name = 'registry_list.html'
    context_object_name = 'registries'


class RegistryUpdateView(UpdateView):
    model = Registry
    form_class = EditingForm
    template_name = 'editing_form.html'
    success_url = "/list"


class RegistryDeleteView(DeleteView):
    model = RegistryFilter
    form_class = CostInputForm
    template_name = 'expense_delete.html'
    success_url = "/list-filter"


class RegistryTypeDeleteView(DeleteView):
    model = Registry
    form_class = CostTypeForm
    template_name = 'expense_delete.html'
    success_url = "/list"


def cost_input_view(request):

    # If this is a POST request we need to process the form data.
    if request.method == 'POST':
        # Create a form instance and populate it
        # with data from the request.
        form = CostInputForm(request.POST)
        # Check whether it is valid.
        if form.is_valid():
            form.save()
            # Does any data require extra processing?
            # If so, do it in form.cleaned_data as required.
            # ...
            # Redirect to a new URL.
            return HttpResponseRedirect(f'/list-filter')
        else:
            # Redirect back to the same page if the data
            # was invalid.
            return render(request, 'cost_input_form.html', {'form': form})

    # If a GET (or any other method) we will create a blank form.
    else:
        form = CostInputForm(request.POST)

    return render(request, 'cost_input_form.html', {'form': form})


def cost_type_view(request):
    if request.method == 'POST':
        form = CostTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/list')
        else:
            return render(request, 'cost_type_form.html', {'form': form})
    else:
        form = CostTypeForm()

    return render(request, 'cost_type_form.html', {'form': form})


class SupplierAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = RegistryFilter.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs



