from rest_framework import routers

from . import views
from django.urls import path, include

from .views import about_view, AboutAPIView

router = routers.DefaultRouter()
router.register(r'about', AboutAPIView)

urlpatterns = [
    path('', about_view),
    path('api/', include(router.urls)),
]