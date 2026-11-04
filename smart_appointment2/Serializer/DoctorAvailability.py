from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.DoctorAvailability import DoctorAvailability


class DocAvailabilitySerializer(ModelSerializer):

    class Meta:
        model = DoctorAvailability
        fields = '__all__'
