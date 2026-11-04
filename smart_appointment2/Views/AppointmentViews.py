from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Serializer.Appointment import AppointmentSerializer
from smart_appointment2.Model.Appointment import Appointment


class AppointmentActions(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
