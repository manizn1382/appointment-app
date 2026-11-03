from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.DoctorSpecialty import DoctorSpecialty


class DocSpecialtySerializer(ModelSerializer):

    class Meta:
        model = DoctorSpecialty
        fields = '__all__'
