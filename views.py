from rest_framework import generics, permissions
from .models import Notes
from .serializers import NotesSerializer


class NotesListCreateView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Notes.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Notes.objects.filter(owner=self.request.user)
