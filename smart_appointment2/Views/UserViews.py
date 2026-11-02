from rest_framework.viewsets import ModelViewSet
from smart_appointment2.Model.Profile import User
from smart_appointment2.Serializer.User import UserSerializer


class UserActions(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
