from rest_framework import serializers
from APIView8.models import Book8

class SerializersBook(serializers.ModelSerializer):
    class Meta:
        model = Book8
        fields = '__all__'