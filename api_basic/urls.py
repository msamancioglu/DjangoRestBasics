from django.urls import path
from .views import article_list, article_detail
#from rest_framework.schemas import get_schema_view

from rest_framework.documentation import include_docs_urls




#schema_view = get_schema_view(title='PasteBin Schema View')

urlpatterns = [
    path('article/', article_list),
    path('article/<int:pk>/', article_detail),
    #path('schemas/', schema_view),
    path('api-docs/', include_docs_urls(title='Rest API', description="All api details here")),

]
