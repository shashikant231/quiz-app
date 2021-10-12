import graphene
from graphene_django import DjangoObjectType
from .models import BookList

# To create GraphQL types for each of our Django models, we are going to subclass
# the DjangoObjectType class which will automatically define GraphQL fields that
# correspond to the fields on the Django models.
class BookListType(DjangoObjectType):
    class Meta:
        model = BookList
        fields = ("id", "book_name", "author", "publisher", "price")

class Query(graphene.ObjectType):
    #This is the data ,where we will perform query
    all_books = graphene.List(BookListType)
    
    #This is the actual query 
    def resolve_all_books(root,info):
        return BookList.objects.all()

schema = graphene.Schema(query=Query)