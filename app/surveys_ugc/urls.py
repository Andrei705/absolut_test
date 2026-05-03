from django.urls import include, path
from rest_framework import routers
from surveys_ugc.views.view_users_undergoing_surveys import UserNoPrivilegesView
from surveys_ugc.views.view_user_privileges import UserPrivilegesView

router = routers.DefaultRouter()
# router.register(r"survey", SurveyViews, basename='survey_views')
router.register(r"user_respose", UserNoPrivilegesView, basename='user_respose')
router.register(r"user_privileges", UserPrivilegesView, basename='privileges')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]