from django.shortcuts import render
from rest_framework import viewsets

from .models import About, AboutBenefit, TeamAbout
from .serializers import AboutSerializer, BenefitSerializer, TeamSerializer


def about_view(request):
    return render(request, 'about.html', {'about_all': About.objects.all(),
                                          'benefit_all': AboutBenefit.objects.all().filter(benefit_draft=True).order_by('benefit_order'),
                                          'team_all': TeamAbout.objects.all().filter(team_draft=True).order_by('team_order')})


class AboutAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class BenefitAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = AboutBenefit.objects.all()
    serializer_class = BenefitSerializer


class TeamAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = TeamAbout.objects.all()
    serializer_class = TeamSerializer
