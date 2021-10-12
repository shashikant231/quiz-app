import graphene
from graphene_django import DjangoObjectType
from .models import Quiz,Question,Answer

# To create GraphQL types for each of our Django models, we are going to subclass
# the DjangoObjectType class which will automatically define GraphQL fields that
# correspond to the fields on the Django models.
class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ("id", "title","category","date_created")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id","quiz","technique","title","difficulty","date_created","is_active")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id","question","answer_text","is_right")

class Query(graphene.ObjectType):
    #This is the data ,where we will perform query
    all_quiz = graphene.List(QuizType)
    all_questions = graphene.List(QuestionType)
    all_answer = graphene.List(AnswerType)
    
    #This is the actual query 
    def resolve_all_quiz(root,info):
        return Quiz.objects.all()
    def resolve_all_questions(root,info):
        return Question.objects.all()
    def resolve_all_answer(root,info):
        return Answer.objects.all()

schema = graphene.Schema(query=Query)