from django.db import models

from django.core.validators import MinLengthValidator,MinValueValidator, MaxValueValidator

MAX_LENGTH_TYPE = 10
MAX_LENGTH_MODEL = 15
MIN_YEAR_MESSAGE = "Year must be between 1999 and 2030!"
MAX_YEAR_MESSAGE = "Year must be between 1999 and 2030!"
MIN_LENGTH_MODEL = message= "Model must be at least 1 character long!"


class Car(models.Model):
    CAR_TYPES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=MAX_LENGTH_TYPE, choices=CAR_TYPES)
    model = models.CharField(max_length=MAX_LENGTH_MODEL, validators=[MinLengthValidator(1, MIN_LENGTH_MODEL)])
    year = models.IntegerField(validators=[
        MinValueValidator(1999, message=MIN_YEAR_MESSAGE),
        MaxValueValidator(2030, message=MAX_YEAR_MESSAGE)
    ])
    image_url = models.URLField(unique=True, error_messages={'unique': "This image URL is already in use! Provide a new one."})
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey('profile.Profile', on_delete=models.CASCADE, related_name='car', editable=False)

    def __str__(self):
        return f"{self.model} - {self.year}"

