from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class CcntactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Silvio Luis',
            slug='silvio-luis',
            photo='http://bit.ly/silvioluis-pic'
        )

    def test_create_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='silviolleite@gmail.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_create_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='12-996263884'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B'
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='silviolleite@gmail.com'
        )
        self.assertEqual('silviolleite@gmail.com', str(contact))
