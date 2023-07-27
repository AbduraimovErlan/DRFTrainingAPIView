from django.urls import path
from APIView5 import views


urlpatterns = [
    path('books5/', views.BookListView.as_view()),
    path('books5/<int:pk>/', views.BookDetailView.as_view()),
]