from django.urls import path

from Rating.views import ExercisesAPIVew, ReviewRatingAPIVew

urlpatterns = [
    path('exercises/', ExercisesAPIVew.as_view()),
    path('<int:pk>/review/', ReviewRatingAPIVew.as_view())
]
