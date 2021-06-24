from rest_framework import serializers
from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SkillTreeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = SkillTree
        fields = '__all__'

class WeaponSerializer(serializers.ModelSerializer):
    trees = SkillTreeSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Weapon
        fields = '__all__'

class WeaponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = [
            'id',
            'name',
            'name_slug',
            'image',
            'main_char',
            'is_selected'
        ]

class BuildSerializer(serializers.ModelSerializer):
    weapon1 = WeaponSerializer(many=False, required=False, read_only=True)
    weapon2 = WeaponSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = Build
        fields = '__all__'

class BuildShortSerializer(serializers.ModelSerializer):
    weapon1 = WeaponsSerializer(many=False, required=False, read_only=True)
    weapon2 = WeaponsSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = Build
        fields = '__all__'
