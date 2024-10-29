from django.db import models
# models.py
from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
    ]
    
    DIET_CHOICES = [
        ('omnivore', 'Omnivore'),
        ('pescatarian', 'Pescatarian'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
    ]
    
    SOCIAL_ACTIVITY_CHOICES = [
        ('never', 'Never'),
        ('often', 'Often'),
        ('sometimes', 'Sometimes'),
    ]

    TRANSPORTATION_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('walk/bicycle', 'Walk/Bicycle'),
    ]

    waste_bag_size = models.CharField(max_length=20)
    waste_bag_count = models.IntegerField(default=0)
    recycle = forms.MultipleChoiceField(
        choices=RECYCLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Do you recycle any materials below?"
    )

    height = models.IntegerField(default=160)  # cm
    weight = models.IntegerField(default=75)    # kg
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    diet = models.CharField(max_length=15, choices=DIET_CHOICES)
    social_activity = models.CharField(max_length=15, choices=SOCIAL_ACTIVITY_CHOICES)

    transportation_mode = models.CharField(max_length=20, choices=TRANSPORTATION_CHOICES)
    vehicle_type = models.CharField(max_length=20, blank=True, null=True)
    vehicle_km = models.IntegerField(default=0)
    air_travel_frequency = models.CharField(max_length=20)

    heating_energy = models.CharField(max_length=20)
    cooking_systems = models.JSONField(default=list)
    energy_efficiency = models.CharField(max_length=20)
    daily_tv_pc_hours = models.IntegerField(default=0)
    daily_internet_hours = models.IntegerField(default=0)

    shower_frequency = models.CharField(max_length=20)
    grocery_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    clothes_monthly = models.IntegerField(default=0)
