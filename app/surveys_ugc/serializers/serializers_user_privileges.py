from rest_framework import serializers
from surveys_ugc.models import Survey, Question, AnswerToQuestion

class AnswerToQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerToQuestion
        fields = ('answer', 'sorted',)


class CreateQuestionSerializer(serializers.ModelSerializer):
    answer_to_question = AnswerToQuestionSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question', 'sorted', 'answer_to_question',)


class CreateSurveySerializer(serializers.ModelSerializer):
    question = CreateQuestionSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('survey_name', 'author', 'question',)

