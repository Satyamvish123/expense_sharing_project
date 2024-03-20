from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.db import migrations
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='expenses_user_set',  
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='expenses_user_set',  
    )

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    split_type = models.CharField(max_length=10)
    split_data = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)

class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    owed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now)

class Migration(migrations.Migration):
    dependencies = [
        ('expenses', 'previous_migration_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]