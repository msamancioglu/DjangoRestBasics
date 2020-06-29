from rest_framework import serializers
from .models import Article
from rest_framework.authtoken.models import Token

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id', 'title', 'author','email', 'date']
        fields = '__all__'

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

