from rest_framework import serializers
from APIView.models import Book1

class SerializersBook(serializers.ModelSerializer):
    class Meta:
        model = Book1
        fields = '__all__'