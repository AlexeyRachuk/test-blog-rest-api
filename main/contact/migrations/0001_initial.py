# Generated by Django 4.1.3 on 2022-11-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_map', models.CharField(max_length=255, verbose_name='Код карты')),
                ('contact_address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('contact_tel', models.CharField(max_length=100, verbose_name='Телефон')),
                ('contact_mail', models.EmailField(max_length=255, verbose_name='Email')),
                ('contact_fb', models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook')),
                ('contact_tw', models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter')),
                ('contact_yt', models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube')),
                ('contact_inst', models.CharField(blank=True, max_length=200, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('form_email', models.CharField(max_length=255, verbose_name='Email')),
                ('form_text', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Заявки с формы',
                'verbose_name_plural': 'Заявки с формы',
            },
        ),
    ]
