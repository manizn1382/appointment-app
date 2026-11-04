from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Serializer.ClinicDoctors import ClinicDocSerializer
from smart_appointment2.Model.ClinicDoctors import ClinicDoctors


class ClinicDocActions(ModelViewSet):
    queryset = ClinicDoctors.objects.all()
    serializer_class = ClinicDocSerializer
