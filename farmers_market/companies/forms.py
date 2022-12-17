from django import forms
from django.core.exceptions import ValidationError

from farmers_market.companies.models import Company
from farmers_market.groceries.models import Grocery
from farmers_market.miscellaneous.form_mixins import DisabledFormMixin


class BaseCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('user',)


class CompanyDeleteForm(DisabledFormMixin, BaseCompanyForm):
    disabled_fields = ('name', 'logo', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            Grocery.objects.all().delete()
            self.instance.delete()
        return self.instance
