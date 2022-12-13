from django import forms

from farmers_market.miscellaneous.form_mixins import DisabledFormMixin
from farmers_market.news.models import News


class BaseNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('author', )


class AddNewsForm(BaseNewsForm):
    pass


class EditNewsForm(BaseNewsForm):
    pass


class DeleteNewsForm(DisabledFormMixin, BaseNewsForm):
    disabled_fields = ('title', 'description', 'image', 'publication', 'author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
