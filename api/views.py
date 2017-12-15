from comment.models import Comment
from rest_framework import viewsets
from .serializers import GetCommentList
# Create your views here.


class GetCommentList(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = GetCommentList
