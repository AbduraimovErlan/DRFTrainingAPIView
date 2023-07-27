from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from APIView8.models import Book8
from APIView8.serializers import SerializersBook


class BookListView(APIView):
    def get(self, request):
        books = Book8.objects.all()
        serializers = SerializersBook(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = SerializersBook(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    def get(self, request, pk=None):
        books = get_object_or_404(Book8.objects.all(), pk=pk)
        serializers = SerializersBook(books)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        books = get_object_or_404(Book8.objects.all(), pk=pk)
        serializers = SerializersBook(books, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        books = get_object_or_404(Book8.objects.all(), pk=pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)