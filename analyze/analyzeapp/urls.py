from django.urls import path,include
from analyzeapp import views

from rest_framework import routers

from analyzeapp.views import QuizQuestionViewset
from .views import QuestionViewset, QuizViewset

router = routers.DefaultRouter()
router.register(r'question',QuestionViewset)
router.register(r'quiz',QuizViewset)

urlpatterns = [
    path('api',include(router.urls)),
    path('',views.welcome,name="welcome"),
    path('create/',views.create_user,name="create_user"),
    path('validate_login/',views.log_in,name="log_user"),
    path('add_quiz/',views.add_quiz,name="add_quiz"),
    path('add_question/',views.add_question,name="add_question"),
    path('test/',views.get_data,name="getdata"),
    path('logout/',views.log_out,name="log_out"),
]