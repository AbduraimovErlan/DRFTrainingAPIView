from rest_framework import serializers
from APIView7.models import Book7

class SerializersBook7(serializers.ModelSerializer):
    class Meta:
        model = Book7
        fields = '__all__'