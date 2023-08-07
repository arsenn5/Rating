from rest_framework import serializers

from Rating.models import Exercises, ReviewRating


class ReviewRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewRating
        fields = ['id', 'rating']


class ExercisesSerializer(serializers.ModelSerializer):
    reviews = ReviewRatingSerializer(many=True, read_only=True)

    class Meta:
        model = Exercises
        fields = '__all__'
