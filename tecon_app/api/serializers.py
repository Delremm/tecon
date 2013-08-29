from rest_framework import serializers
from tecon_app.models import Trial


class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = ('title', 'description', 'data', 'created')
