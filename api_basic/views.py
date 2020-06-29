from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from .models import Article
from rest_framework.authtoken.models import Token
from .serializers import ArticleSerializer, TokenSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@login_required
def getToken(request):
    return HttpResponse(request.POST.get('username'))


##Token lsit create

class TokenList(generics.ListCreateAPIView):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Token.objects.all()
    serializer_class = TokenSerializer



class TokenDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


#Generic based view for GET and POST (list and create)

class ArticleList(generics.ListCreateAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



#Class based api view
class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    # Firstly, lets find requested article
    article = get_object_or_404(Article, pk=pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


