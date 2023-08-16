from rest_framework import serializers
from .models import Conference
class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields  = ['confId', 'confName', 'detailConf', 'confImages']