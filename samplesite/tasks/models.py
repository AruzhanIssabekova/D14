from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_title(value):
    if not re.match(r'^[a-zA-Z0-9\s]{3,50}$', value):
        raise ValidationError(
            _('Название задачи должно состоять только из букв, цифр и пробелов, и иметь длину от 3 до 50 символов.')
        )

def validate_description(value):
    if not re.match(r'^[a-zA-Z0-9\s]{10,}$', value):
        raise ValidationError(
            _('Описание задачи должно состоять только из букв, цифр и пробелов, и иметь длину не менее 10 символов.')
        )

def validate_due_date(value):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(value)):
        raise ValidationError(
            _('Неверный формат даты. Используйте формат ГГГГ-ММ-ДД.')
        )

def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('Value must be zero or a positive number.')
        )

class Task(models.Model):
    title = models.CharField(max_length=50, validators=[validate_title])
    description = models.TextField(validators=[validate_description])
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(validators=[validate_due_date])
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    completed = models.BooleanField(default=False)
    positive_number = models.PositiveIntegerField(validators=[validate_positive])

    def id_and_title(self):
        return f"{self.id}: {self.title}"

    def sum_priority_completed(self):
        priority_values = {'low': 1, 'medium': 2, 'high': 3}
        priority_value = priority_values.get(self.priority, 0)
        completed_value = 1 if self.completed else 0
        return priority_value + completed_value



