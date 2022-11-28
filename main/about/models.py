from django.db import models
from solo.models import SingletonModel


class About(SingletonModel):
    about_banner = models.ImageField('Баннер на странице', upload_to='images/')
    about_title = models.CharField('Заголовок на странице', max_length=60)
    about_text = models.TextField('Описание на странице')

    def __str__(self):
        return "О нас"

    class Meta:
        verbose_name = "О нас"


class AboutBenefit(models.Model):
    ICONS = [
        ('fas fa-bezier-curve fa-4x tm-color-primary', 'иконка 1'),
        ('fas fa-users-cog fa-4x tm-color-primary', 'иконка 2'),
        ('fab fa-creative-commons-sampling fa-4x tm-color-primary', 'иконка 3')
    ]
    benefit_icon = models.CharField('Иконка', choices=ICONS, max_length=60)
    benefit_title = models.CharField('Заголовок', max_length=60)
    benefit_text = models.TextField('Описание приемущества')
    benefit_order = models.PositiveSmallIntegerField('Порядок', default=0)
    benefit_draft = models.BooleanField('Публикация', default=True)
    benefits_on_about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='benefits_id', default='')

    def __str__(self):
        return "Приемущества"

    class Meta:
        verbose_name = "Приемущества"
        verbose_name_plural = "Приемущества"


class TeamAbout(models.Model):
    team_name = models.CharField('Имя', max_length=100)
    team_post = models.CharField('Должность', max_length=100)
    team_text = models.TextField('Описание')
    team_photo = models.ImageField('Фото', upload_to='images/')
    team_order = models.PositiveSmallIntegerField('Порядок', default=0)
    team_draft = models.BooleanField('Публикация', default=True)
    team_on_about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='team_id', default='')

    def __str__(self):
        return "Команда"

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"
