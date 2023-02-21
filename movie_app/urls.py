from django.urls import path
from .views import test, directors_list_view, detail_director_view, movies_list_view, detail_movie_view,\
    review_list_view, detail_review, show_movies_reviews

urlpatterns = [
    path('api/v1/test/', test),
    path('api/v1/directors/', directors_list_view),
    path('api/v1/directors/<int:id>/', detail_director_view),
    path('api/v1/movies/', movies_list_view),
    path('api/v1/movies/<int:id>/', detail_movie_view),
    path('api/v1/reviews/', review_list_view),
    path('api/v1/reviews/<int:id>/', detail_review),
    path('api/v1/movies/reviews/', show_movies_reviews)

]