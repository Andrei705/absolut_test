
from django.contrib.admin import action
from django.db.models import F, Count, Prefetch
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework import status, response
from surveys_ugc.models import Survey, UserResponse, AnswerToQuestion, Question
from surveys_ugc.serializers.serializers_user_no_privalages import CreateUserResponseSerializer, SurveyOutputSerializer


# class SurveyViews(mixins.ListModelMixin, viewsets.GenericViewSet):
#
#     @swagger_auto_schema(method='GET')
#     def get(self, request):
#         survey_id = request.query_params.get('survey')
#         author_name = request.query_params.get('author')
#
#         queryset = Survey.objects.select_related(
#             'author__full_name'
#         ).filter(
#             question_survey__id=survey_id,
#             author__full_name=author_name
#         ).values(
#             'question_survey__question',
#             'question_survey__answer',
#             'survey_name',
#         )
#         return response.Response(queryset, status=status.HTTP_200_OK)


class UserNoPrivilegesView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):

    queryset = UserResponse.objects.all()
    serializer_class = CreateUserResponseSerializer


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_QUERY,
                description='id опроса',
                type='int'
            )
        ]
    )

    def list(self, request):
        syrvey_id = request.query_params['id']

        queryset = Survey.objects.only(
            'survey_name',
            'id'
        ).filter(
            pk=syrvey_id
        ).prefetch_related(
            'question_survey',
            'question_survey__answertoquestion_question',
            'question_survey__answertoquestion_question__userresponse_answertoquestion',
        )


        return response.Response(
            data=SurveyOutputSerializer(queryset, many=True).data,
            status=status.HTTP_200_OK
        )



