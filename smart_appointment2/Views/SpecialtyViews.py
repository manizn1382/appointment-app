from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.Specialty import Specialty
from smart_appointment2.Serializer.Specialty import SpecialtySerializer


class SpecialtyActions(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer