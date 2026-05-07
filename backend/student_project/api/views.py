from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'phone']