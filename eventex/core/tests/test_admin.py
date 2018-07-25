from django.test import TestCase
from django.utils.html import format_html

from eventex.core.admin import SpeakerModelAdmin, Speaker, admin, ContactInLine, TalkModelAdmin
from eventex.core.models import Contact, Talk, Course


class SpeakerModelAdminTest(TestCase):
    def setUp(self):
        self.s = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            description='Programadora e almirante.'
        )
        self.s.contact_set.create(kind=Contact.EMAIL, value='silviolleite@gmail.com')
        self.s.contact_set.create(kind=Contact.PHONE, value='12-12345678')
        self.model_admin = SpeakerModelAdmin(self.s, admin.site)

    def test_inline(self):
        self.assertListEqual([ContactInLine], self.model_admin.inlines)

    def test_inline_has_extra(self):
        self.assertEqual(1, self.model_admin.inlines[0].extra)

    def test_inline_has_model_contact(self):
        self.assertIs(Contact, self.model_admin.inlines[0].model)

    def test_populated_fields(self):
        """Slug Must be auto populate with the field name"""
        expect = {'slug': ('name',)}
        self.assertDictEqual(expect, self.model_admin.prepopulated_fields)

    def test_has_fields(self):
        expected = ['name', 'photo_img', 'website_link', 'email', 'phone']
        self.assertListEqual(expected, self.model_admin.list_display)

    def test_website_link(self):
        expected = format_html('<a href="{0}">{0}</a>', Speaker.website)
        self.assertEqual(expected, self.model_admin.website_link(Speaker))

    def test_photo_link(self):
        expected = format_html('<img width="32px" src="{0}" />', Speaker.photo)
        self.assertEqual(expected, self.model_admin.photo_img(Speaker))

    def test_has_first_email_from_contact(self):
        self.assertEqual('silviolleite@gmail.com', str(self.model_admin.email(self.s)))

    def test_has_first_phone_from_contact(self):
        self.assertEqual('12-12345678', str(self.model_admin.phone(self.s)))


class TalkModelAdminTest(TestCase):
    def setUp(self):
        Talk.objects.create(
            title='Título da Palestra',
        )
        Talk.objects.create(
            title='Título da Palestra 2',
        )
        Course.objects.create(
            title='Título do curso',
            slots=20
        )
        self.model_admin = TalkModelAdmin(Talk, admin.site)

    def test_queryset(self):
        talks = self.model_admin.get_queryset(None).count()
        self.assertEqual(2, talks)

