from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.DoctorSpecialty import DoctorSpecialty
from smart_appointment2.Serializer.DoctorSpecialty import DocSpecialtySerializer


class DocSpecialtyActions(ModelViewSet):
    queryset = DoctorSpecialty.objects.all()
    serializer_class = DocSpecialtySerializer

