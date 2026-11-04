from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.DoctorAvailability import DoctorAvailability
from smart_appointment2.Serializer.DoctorAvailability import DocAvailabilitySerializer


class DocAvailabilityActions(ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DocAvailabilitySerializer
