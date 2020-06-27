from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from django.views.decorators.csrf import csrf_exempt

from .models import Article
from .serializers import ArticleSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from django.shortcuts import get_object_or_404

# Create your views here.
#@login_required(login_url='/accounts/login')
@csrf_exempt
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many= True)
        return JsonResponse(serializer.data, safe= False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)


@csrf_exempt
def article_detail(request, pk):
    # Firstly, lets find requested article
    article = get_object_or_404(Article, pk=pk)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe= False)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)


    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(pk)


