from django import forms

from farmers_market.miscellaneous.models import Review


class ReviewGroceryForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review', 'customer_rating',)

        widgets = {
            'review': forms.Textarea(
                attrs={
                    'placeholder': 'Add a review...'
                }
            ),
        }
