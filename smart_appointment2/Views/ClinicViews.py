from smart_appointment2.Serializer.Clinic import ClinicSerializer
from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.Clinic import Clinic


class ClinicActions(ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    lookup_field = 'id'


