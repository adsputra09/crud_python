from django.shortcuts import render
from django. shortcuts import get_object_or_404
from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import News, Topik
from .serializers import newsSerializer


class newsList(APIView):
 
    def get(self, request):
        berita = News.objects.all()
        serializer = newsSerializer(berita, many=True)
        return Response(serializer.data)

    def put(self, request):
        serializer = newsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class detailList(APIView):
    def get(self, request, pk):
        berita = get_object_or_404(News, pk=pk)
        serializer = newsSerializer(berita)
        return Response(serializer.data)

    def delete(self, request, pk):
        berita = get_object_or_404(News, pk=pk)
        berita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class filterTopik(filters.FilterSet):
#     topik = filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = News
#         fields = ('judul')