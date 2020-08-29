from django.urls import path

from .views import MainView, cost_type_view, RegistryTypeListView, RegistryFilterListView, cost_input_view, \
    RegistryUpdateView, RegistryDeleteView, SupplierAutocomplete, RegistryTypeDeleteView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('cost-input-form/', cost_input_view, name='cost_input_view'),
    path('cost-type-form/', cost_type_view, name='cost_type_view'),
    path('list-filter', RegistryFilterListView.as_view(), name='registry_filter_list'),
    path('list/', RegistryTypeListView.as_view(), name='registry_type_list'),
    path('update/<int:pk>', RegistryUpdateView.as_view(), name='update_view'),
    path('delete_type/<int:pk>', RegistryTypeDeleteView.as_view(), name='delete_type_view'),
    path('delete/<int:pk>', RegistryDeleteView.as_view(), name='delete_view'),
    path('supplier-autocomplete', SupplierAutocomplete.as_view(), name='supplier-autocomplete')
]

