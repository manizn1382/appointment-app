from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Appointment import Appointment


class AppointmentSerializer(ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'
