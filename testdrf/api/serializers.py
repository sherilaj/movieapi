from rest_framework import serializers
from . models import Movie,Comment
from django.contrib.auth import get_user_model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = get_user_model()
        fields = ('username','password')
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'