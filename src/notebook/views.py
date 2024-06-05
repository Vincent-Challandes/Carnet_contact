from rest_framework import permissions, viewsets
from notebook.models import Contact
from notebook.serializers import ContactSerializer


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contact to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
