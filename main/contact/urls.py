from rest_framework import routers

from . import views
from django.urls import path, include

from .views import contact_page

# router = routers.DefaultRouter()
# router.register(r'about', AboutAPIView)

urlpatterns = [
    path('', contact_page),
    # path('api/', include(router.urls)),
]
