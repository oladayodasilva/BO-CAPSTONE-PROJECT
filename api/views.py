from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions, filters

from .models import Property
from .serializers import PropertySerializer, RegisterSerializer
from .permissions import IsOwnerOrReadOnly


# ---------------------------
# Property ViewSet
# ---------------------------
class PropertyViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing properties.
    Only authenticated users can create/update/delete.
    Users can only modify their own properties.
    Supports searching and ordering.
    """
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'property_type', 'address']
    ordering_fields = ['price', 'created_at']

    def get_queryset(self):
        """
        Return properties owned by the logged-in user.
        """
        return Property.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Set the owner of the property to the logged-in user.
        """
        serializer.save(owner=self.request.user)


# ---------------------------
# User Registration API
# ---------------------------
class RegisterAPIView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Allows anyone to create a new user account.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]