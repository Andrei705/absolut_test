from django.db import transaction
from django.db.models import Count
from django.db.models.functions import JSONObject
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, views, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from surveys_ugc.models import Survey, Question, AnswerToQuestion
from surveys_ugc.serializers.serializers_update_user_privileges import UpdateSurveySerializer, UpdateQuestionSerializer
from surveys_ugc.serializers.serializers_user_privileges import CreateSurveySerializer


class UserPrivilegesView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    @transaction.atomic
    @swagger_auto_schema(request_body=CreateSurveySerializer())
    def create(self, request):
        data = CreateSurveySerializer(data=request.data).initial_data
        question = data.pop('question')

        survey_id:int = self.create_survey(data=data)
        question_id:list = self.create_question(data=question)

        self.create_answer(question_id=question_id, survey_id=survey_id, data=question)

        return Response({'id':1}, status=status.HTTP_201_CREATED)

    @staticmethod

    def create_survey(data: dict) -> int:
        queryset = Survey.objects.create(
            survey_name=data['survey_name'],
            author_id=data['author']
        )
        return queryset.id

    @staticmethod
    def create_question(data: dict) -> list:
        question = Question.objects.bulk_create(
            [
                Question(
                    question=data[index].get('question'),
                    sorted=data[index].get('sorted')
                )
                for index in range(0, len(data))
            ]

        )
        return [field.id for field in question]

    @staticmethod
    def create_answer(question_id: list, survey_id: int, data: dict) -> None:
        l1 = 0
        l2 = 0
        res = []
        while True:

            if l1 <= len(question_id) - 1:
                if l2 <= len(data[l1].get('answer_to_question')) - 1:
                    res.append(
                        AnswerToQuestion(
                            answer=data[l1].get('answer_to_question')[l2].get('answer'),
                            survey_id=survey_id,
                            question_id=question_id[l1],
                            sorted=data[l1].get('answer_to_question')[l2].get('sorted')
                        )
                    )
                    l2 += 1
                else:
                    l2 = 0
                    l1 += 1
            else:
                break

        AnswerToQuestion.objects.bulk_create(res)

    @transaction.atomic
    @swagger_auto_schema(request_body=UpdateSurveySerializer())
    def partial_update(self, request, pk=None):
        data = CreateSurveySerializer(data=request.data).initial_data
        queryset = Survey.objects.filter(pk=pk)
        queryset.update(**data)
        return Response(queryset.values(), status=status.HTTP_201_CREATED)

    @transaction.atomic
    @swagger_auto_schema(request_body=UpdateQuestionSerializer())
    def update(self, request, pk=None):
        data = UpdateQuestionSerializer(data=request.data).initial_data
        queryset = Question.objects.filter(pk=pk)
        queryset.update(**data)
        return Response(queryset.values(), status=status.HTTP_201_CREATED)


class UserNoPrivilegesView(
    mixins.CreateModelMixin,
    # mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):

    def create(self, request):





