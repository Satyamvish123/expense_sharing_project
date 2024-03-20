from django.urls import path
from .views import UserViewSet, ExpenseViewSet, ExpenseParticipantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'expense-participants', ExpenseParticipantViewSet)

urlpatterns = router.urls