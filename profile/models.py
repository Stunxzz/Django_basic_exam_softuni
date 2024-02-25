from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
MAX_LENGTH_PASSWORD = 20
MAX_LENGTH_NAME = 25
MAX_LENGTH_USERNAME = 15
USER_NAME_MIN_MESSAGE = "Username must be at least 3 chars long!"
USER_NAME_MIN_LETTERERS_DIGIT = "Username must contain only letters, digits, and underscores!"
AGE_TEXT = "Age requirement: 21 years and above."


def validate_username(value):
    if not value.isalnum() and '_' not in value:
        raise ValidationError(USER_NAME_MIN_LETTERERS_DIGIT)


class Profile(models.Model):
    username = models.CharField(max_length=MAX_LENGTH_USERNAME, validators=[
        MinLengthValidator(3, message=USER_NAME_MIN_MESSAGE),
        validate_username
    ])
    email = models.EmailField()
    age = models.IntegerField(help_text=AGE_TEXT)
    password = models.CharField(max_length=MAX_LENGTH_PASSWORD)
    first_name = models.CharField(max_length=MAX_LENGTH_NAME, blank=True, null=True)
    last_name = models.CharField(max_length=MAX_LENGTH_NAME, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
