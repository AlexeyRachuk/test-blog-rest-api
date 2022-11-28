from django.contrib import admin
from solo.admin import SingletonModelAdmin

from django import forms
from .models import Contact, ContactForm


@admin.register(Contact)
class AdminContact(SingletonModelAdmin):
    fields = ['contact_map', 'contact_address', 'contact_tel', 'contact_mail', 'contact_fb', 'contact_tw',
              'contact_yt', 'contact_inst']


@admin.register(ContactForm)
class AdminContactsForm(admin.ModelAdmin):
    list_display = ('form_name',)
