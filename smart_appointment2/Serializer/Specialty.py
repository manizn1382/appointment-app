from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Specialty import Specialty


class SpecialtySerializer(ModelSerializer):

    class Meta:
        model = Specialty
        fields = '__all__'
