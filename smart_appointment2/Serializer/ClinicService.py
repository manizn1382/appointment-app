from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.ClinicService import ClinicService


class ClinicServiceSerializer(ModelSerializer):

    class Meta:
        model = ClinicService
        fields = "__all__"
