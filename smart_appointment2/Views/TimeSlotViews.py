from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.TimeSlot import TimeSlot
from smart_appointment2.Serializer.TimeSlot import TimeSlotSerializer


class TimeSlotActions(ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
