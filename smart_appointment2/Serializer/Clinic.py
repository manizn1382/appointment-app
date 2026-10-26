from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Clinic import Clinic


class ClinicSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'
