from rest_framework import serializers

from surveys_ugc.models import AnswerToQuestion, UserResponse


class CreateUserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserResponse
        fields = ('answer', 'author', 'answer_to_question',)
