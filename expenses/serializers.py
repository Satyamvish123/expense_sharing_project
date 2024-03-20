from rest_framework import serializers
from .models import User, Expense, ExpenseParticipant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile_number')

class ExpenseSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Expense
        fields = ('id', 'user', 'amount', 'split_type', 'split_data', 'created_at')

class ExpenseParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    expense = ExpenseSerializer()

    class Meta:
        model = ExpenseParticipant
        fields = ('id', 'user', 'expense', 'amount', 'owed_amount', 'created_at')