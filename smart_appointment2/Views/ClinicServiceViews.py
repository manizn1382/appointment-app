from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.ClinicService import ClinicService
from smart_appointment2.Serializer.ClinicService import ClinicServiceSerializer


class ClinicServiceActions(ModelViewSet):
    queryset = ClinicService.objects.all()
    serializer_class = ClinicServiceSerializer
