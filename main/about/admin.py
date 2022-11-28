from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import About, AboutBenefit, TeamAbout


class AboutBenefitInline(admin.TabularInline):
    model = AboutBenefit
    extra = 1


class TeamAboutInline(admin.TabularInline):
    model = TeamAbout
    extra = 1


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    inlines = [AboutBenefitInline, TeamAboutInline, ]