from rest_framework import generics
from .models import Record
from .serializers import RecordSerializer
from .permissions import IsAuthorOrReadOnly


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_queryset(self):
        return self.request.user.employees.all()

    def perform_create(self, serializer):
        serializer.save(employee_username=self.request.user)


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
