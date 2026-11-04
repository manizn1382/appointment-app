from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.Payment import Payment
from smart_appointment2.Serializer.Payment import PaySerializer


class PayActions(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaySerializer