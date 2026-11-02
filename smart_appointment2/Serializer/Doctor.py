from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Doctor import Doctor


class DoctorSerializer(ModelSerializer):



    class Meta:
        model = Doctor
        fields = ['medicalLicense', 'user']

