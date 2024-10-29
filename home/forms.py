# forms.py
from django import forms
from .models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = [
#             'height', 
#             'weight', 
#             'gender', 
#             'diet', 
#             'social_activity',
#             'waste_bag_size',
#             'waste_bag_count',
#             'recycles',
#             'transportation_mode', 
#             'vehicle_type', 
#             'vehicle_km',
#             'air_travel_frequency',
#             'heating_energy',
#             'cooking_systems',
#             'energy_efficiency',
#             'daily_tv_pc_hours',
#             'daily_internet_hours',
#             'shower_frequency',
#             'grocery_bill',
#             'clothes_monthly',
#         ]
#         widgets = {
#             'recycles': forms.CheckboxSelectMultiple(),
#             'cooking_systems': forms.CheckboxSelectMultiple(),
#         }


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'gender', 'diet', 'social_activity']

class TravelInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['transportation_mode', 'vehicle_type', 'flying_times']

class WasteInfoForm(forms.ModelForm):
    class Meta:
        model = UserModel 
        fields = ["size_of_bag","number_of_bags", "recycle_items"]
