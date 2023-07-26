from django.urls import path
from APIView4 import views

urlpatterns = [
    path('books4/', views.BookListView.as_view()),
    path('books4/<int:pk>/', views.BookDetailView.as_view()),
]