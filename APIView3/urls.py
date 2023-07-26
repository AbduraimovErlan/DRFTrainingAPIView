from django.urls import path
from APIView3 import views


urlpatterns = [
    path('books3/', views.BookListView.as_view()),
    path('books3/<int:pk>/', views.BookDetailView.as_view()),
]