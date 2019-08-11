from rest_framework import serializers

from historytoday.models import models as hst_models


class HistoryStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = hst_models.HistoryStory
        fields = '__all__'
        depth = 0
