from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from analyzeapp.models import Question, Quiz
from analyzeapp.serializer import QuestionSerialzer, QuizSerializer

#welcome screen
def welcome(request):
    if request.user.is_authenticated:
        return render(request,"quiz.html")
    return render(request,"index.html")

@login_required()
def get_data(request):
    return render(request,"quiz.html")


#view for creating user
def create_user(request):
    if request.method == 'POST':
        name =  request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(name,email,password)
    return render(request,"index.html")

#view for logging in
def log_in(request):
    print("out")
    if request.method == 'POST':
        print("in")
        username = request.POST.get("username")
        password  = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse("success")
            else:
                return HttpResponse("disabled account")
        else:
            return HttpResponse("invalid credentials")
@login_required()
def log_out(request):
    logout(request)
    return render(request,"index.html")

@login_required()
def add_quiz(request):
    if request.method == 'POST':
        print("hello")
        quiz_name = request.POST.get("quiz_name")
        user = request.POST.get("user")
        quiz = Quiz()
        quiz.name = quiz_name
        quiz.user = User.objects.get(qq=user)
        quiz.save()
        return HttpResponse(quiz.id)

@login_required()
def add_question(request):
    if request.method == "POST":
        question  = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        answer = request.POST.get("answer")
        quiz = request.POST.get("quiz")
        q = Question()
        q.question = question
        q.option1 = option1
        q.option2 = option2
        q.option3 = option3
        q.option4 = option4
        q.answer = answer
        q.quiz = Quiz.objects.get(qq=int(quiz))
        q.save()
        return HttpResponse("success")

#viewsets for rest_framework
class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialzer


class QuizViewset(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizQuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerialzer
    queryset = Question.objects.filter(quiz_id = 1)
    def get_queryset(self):
        return Question.objects.filter(quiz_id=self.kwargs.get('qq'))

