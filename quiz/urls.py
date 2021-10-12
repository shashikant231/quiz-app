from django.contrib import admin
from django.urls import path,include
from quiz.schema import schema

from graphene_django.views import GraphQLView

urlpatterns = [
     path("v1/", GraphQLView.as_view(graphiql=True,schema = schema)),
]