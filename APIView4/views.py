from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from APIView4.serializers import SerializersBook4
from APIView4.models import Book4



class BookListView(APIView):
    def get(self, request):
        books = Book4.objects.all()
        serializers = SerializersBook4(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = SerializersBook4(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk=None):
        books = get_object_or_404(Book4.objects.all(), pk=pk)
        serializers = SerializersBook4(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        books = get_object_or_404(Book4.objects.all(), pk=pk)
        serializers = SerializersBook4(books, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        books = get_object_or_404(Book4.objects.all(), pk=None)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
