from rest_framework import serializers
from surveys_ugc.models import Survey, Question


class UpdateSurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('survey_name',)
        read_only_fields = ('id', 'author', 'survey_name', )


class UpdateQuestionSerializer(serializers.ModelSerializer):
    sorted = serializers.IntegerField(required=True)

    class Meta:
        model = Question
        fields = ('question', 'sorted', )