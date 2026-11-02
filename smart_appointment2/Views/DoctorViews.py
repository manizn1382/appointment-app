from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Serializer.Doctor import DoctorSerializer
from smart_appointment2.Model.Doctor import Doctor


class DoctorActions(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
