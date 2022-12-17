from django import forms

from farmers_market.groceries.models import Grocery


class AddGroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        exclude = ('slug', 'user', 'company')
        # fields = ('name', 'category', 'quality_rating', 'expiry_date', 'image_url',)


class EditGroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        exclude = ('quality_rating', 'user', 'company', 'slug',)


class DeleteGroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def _set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
