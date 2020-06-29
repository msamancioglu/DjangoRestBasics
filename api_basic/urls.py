from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleList, ArticleDetail, TokenList, TokenDetail, getToken
#from rest_framework.schemas import get_schema_view

from rest_framework.documentation import include_docs_urls


#schema_view = get_schema_view(title='PasteBin Schema View')

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetail.as_view()),
    path('api-docs/', include_docs_urls(title='Rest API', description="All api details here")),
    path('token/', TokenList.as_view()),
    path('token/<int:user>/', TokenDetail.as_view()),
    path('gettoken/', getToken)

]
