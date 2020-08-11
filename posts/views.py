from rest_framework import viewsets
from .models import Article
from .serializer import ArticleSerializer

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()