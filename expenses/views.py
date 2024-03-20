
from rest_framework import viewsets
from .models import User, Expense, ExpenseParticipant
from .serializers import UserSerializer, ExpenseSerializer, ExpenseParticipantSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseParticipantViewSet(viewsets.ModelViewSet):
    queryset = ExpenseParticipant.objects.all()
    serializer_class = ExpenseParticipantSerializer