from rest_framework import serializers
from APIView6.models import Book6


class SerializersBook(serializers.ModelSerializer):
    class Meta:
        model = Book6
        fields = '__all__'