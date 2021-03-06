from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_format_with_separator(self):
        """CPF must accept xxx.xxx.xxx-xx"""
        form = self.make_validated_form(cpf='111.111.111-11')
        self.assertFalse(form.errors)

    def test_cpf_is_digit(self):
        """CPF must only accept digit"""
        form = self.make_validated_form(cpf='abc12345678')
        self.assertFormErrorCode(form, 'cpf', 'format')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        form = self.make_validated_form(name='SILVIO luis')
        self.assertEqual('Silvio Luis', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email must be optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone must be optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Must inform email or phone"""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def make_validated_form(self, **kwargs):
        valid = dict(name='Silvio Luis', cpf='12345678901', email='silviolleite@gmail.com', phone='12-121212122')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form


class FormRegressionTest(TestCase):
    def test_must_use_cleaned_data_get(self):
        """Must use cleaned_data.get"""
        invalid_data = dict(name='Silvio Luis', cpf='12345678901', email='asdf', phone='')
        form = SubscriptionForm(invalid_data)
        self.assertEqual(False, form.is_valid())
