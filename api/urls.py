from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r"properties", PropertyViewSet, basename="property")

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
]

urlpatterns += router.urls
