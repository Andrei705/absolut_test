from django.db.models import F
from rest_framework.views import APIView
from rest_framework import status, response
from models import Survey


class SurveyViews(APIView):

    def get(self, request):
        survey_id = request.query_params.get('survey')
        author_name = request.query_params.get('author')

        queryset = Survey.objects.select_related(
            'author__full_name'
        ).filter(
            question_survey__id=survey_id,
            author__full_name=author_name
        ).values(
            'question_survey__question',
            'question_survey__answer',
            'survey_name',
        )
        return response.Response(queryset, status=status.HTTP_200_OK)