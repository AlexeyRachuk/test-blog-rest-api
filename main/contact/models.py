from django.db import models
from solo.models import SingletonModel


class Contact(SingletonModel):
    contact_map = models.CharField('Код карты', max_length=255)
    contact_address = models.CharField('Адрес', max_length=150)
    contact_tel = models.CharField('Телефон', max_length=100)
    contact_mail = models.EmailField('Email', max_length=255)
    contact_fb = models.CharField('Facebook', max_length=200, blank=True, null=True)
    contact_tw = models.CharField('Twitter', max_length=200, blank=True, null=True)
    contact_yt = models.CharField('Youtube', max_length=200, blank=True, null=True)
    contact_inst = models.CharField('Instagram', max_length=200, blank=True, null=True)

    def __str__(self):
        return "Контакты"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class ContactForm(models.Model):
    form_name = models.CharField('Имя', max_length=100)
    form_email = models.CharField('Email', max_length=255)
    form_text = models.TextField('Сообщение')

    class Meta:
        verbose_name = "Заявки с формы"
        verbose_name_plural = "Заявки с формы"

    def __str__(self):
        return "Заявки с формы"
