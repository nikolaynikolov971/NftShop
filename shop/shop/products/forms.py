from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator

from shop.products.models import Product
from shop.profiles.validators import only_digits_validator


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=30)


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'image')


class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    bots_catcher = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_bots_catcher(self):
        value = self.cleaned_data['bots_catcher']

        if value:
            raise ValidationError('Bot was caught.')


class CardForm(forms.Form):
    number = forms.CharField(validators=[only_digits_validator, MinLengthValidator(16), MaxLengthValidator(16)])
    cvv = forms.CharField(validators=[only_digits_validator, MinLengthValidator(3), MaxLengthValidator(3)])
