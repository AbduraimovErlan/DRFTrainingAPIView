from django.urls import path
from APIView9 import views


urlpatterns = [
    path('books9/', views.BookListView.as_view()),
    path('books9/<int:pk>/', views.BookDetailView.as_view()),
]