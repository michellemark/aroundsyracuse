from django.forms import ModelForm, TextInput, EmailField, EmailInput, CheckboxInput, Select

from sellers.models import SellerProfile
from sellers.utilities import bleachinput, validate_zip


class SellerProfileForm(ModelForm):

    class Meta:
        model = SellerProfile
        fields = ("first_name", "last_name", "email",
                  "phone_number", "is_phone_mobile", "permission_to_text",
                  "address", "city", "zip_code", "property_type")
        widgets = {
            'first_name': TextInput(
                attrs={'required': 'required',
                       'maxlength': '30',
                       'class': 'form-control'}
            ),
            'last_name': TextInput(
                attrs={'required': 'required',
                       'maxlength': '30',
                       'class': 'form-control'}
            ),
            'email': EmailInput(
                attrs={'required': 'required',
                       'class': 'form-control',
                       'maxlength': '255'}
            ),
            'phone_number': TextInput(
                attrs={'maxlength': '10',
                       'class': 'form-control'}
            ),
            'is_phone_mobile': CheckboxInput(
                attrs={'class': 'checkbox'}
            ),
            'permission_to_text': CheckboxInput(
                attrs={'class': 'checkbox'}
            ),
            'address': TextInput(
                attrs={'class': 'form-control',
                       'maxlength': '100'}
            ),
            'city': TextInput(
                attrs={'maxlength': '50',
                       'class': 'form-control'}
            ),
            'zip_code': TextInput(
                attrs={'maxlength': '10',
                       'class': 'form-control'}
            ),
            'property_type': Select(
                choices=[],
                attrs={'maxlength': '1',
                       'class': 'form-control',
                       'required': 'required'}
            )
        }

    def clean_first_name(self):
        first_name = bleachinput(self.cleaned_data.get('first_name'))

        return first_name.title()

    def clean_last_name(self):
        last_name = bleachinput(self.cleaned_data.get('last_name'))

        return last_name.title()

    def clean_address(self):
        address = bleachinput(self.cleaned_data.get('address'))

        return address.title()

    def clean_city(self):
        city = bleachinput(self.cleaned_data.get('city'))

        return city.title()

    def clean_zipcode(self):
        given_zip = self.cleaned_data.get('zipcode')

        if given_zip:
            given_zip = validate_zip(given_zip)

        return given_zip
