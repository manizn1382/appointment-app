from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.TimeSlot import TimeSlot


class TimeSlotSerializer(ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = '__all__'
