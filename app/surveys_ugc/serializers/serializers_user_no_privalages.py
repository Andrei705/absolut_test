from rest_framework import serializers

from surveys_ugc.models import AnswerToQuestion, UserResponse, Question, Survey


class CreateUserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserResponse
        fields = ('answer', 'author_id', 'answer_to_question_id',)


    def create(self, validated_data):
        UserResponse.objects.create(**validated_data)
        return validated_data



class UserResponseOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = ('answer',)


class AnswerToQuestionOutputSerializer(serializers.ModelSerializer):
    userresponse_answertoquestion = UserResponseOutputSerializer(many=True)

    class Meta:
        model = AnswerToQuestion
        fields = ('answer', 'sorted', 'userresponse_answertoquestion',)



class QuestionOutputSerializer(serializers.ModelSerializer):
    answertoquestion_question = AnswerToQuestionOutputSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question', 'sorted', 'answertoquestion_question',)


class SurveyOutputSerializer(serializers.ModelSerializer):
    question_survey = QuestionOutputSerializer(many=True)

    class Meta:
        model = Survey
        fields = ('survey_name', 'question_survey',)