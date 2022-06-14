from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'day', 'check_in', 'check_out',)
        model = Record
