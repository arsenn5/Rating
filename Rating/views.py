from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from Rating.models import Exercises, ReviewRating
from Rating.serializers import ExercisesSerializer, ReviewRatingSerializer


class ExercisesAPIVew(ListAPIView):
    queryset = Exercises.objects.all()
    serializer_class = ExercisesSerializer


class ReviewRatingAPIVew(CreateAPIView):
    queryset = ReviewRating.objects.all()
    serializer_class = ReviewRatingSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        exercises = Exercises.objects.get(pk=pk)

        if exercises.number_rating == 0:
            exercises.avg_number = serializer.validated_data['rating']
        else:
            exercises.avg_number = (exercises.avg_number + serializer.validated_data['rating']) / 2
        exercises.number_rating = exercises.number_rating + 1
        exercises.save()

        serializer.save(exercises=exercises)
