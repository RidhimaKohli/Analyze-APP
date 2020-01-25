from rest_framework import serializers

from analyzeapp.models import Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id','name','user']

class QuestionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question','option1','option2','option3','option4','answer','exam']
