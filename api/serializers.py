from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Word, UserWordProgress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class UserWordProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWordProgress
        fields = ['id', 'word', 'known', 'lastLearned', 'correctAnswersCount', 'repetitionInterval', 'lastCorrectAnswerDate', 'mnemonic']
        extra_kwargs = {
            'known': {'required': False},
            'lastLearned': {'required': False},
            'correctAnswersCount': {'required': False},
            'repetitionInterval': {'required': False},
            'lastCorrectAnswerDate': {'required': False},
            'mnemonic': {'required': False},
        }