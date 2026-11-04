from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.ClinicDoctors import ClinicDoctors


class ClinicDocSerializer(ModelSerializer):
    class Meta:
        model = ClinicDoctors
        fields = '__all__'
