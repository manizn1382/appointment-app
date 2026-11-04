from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Payment import Payment


class PaySerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
