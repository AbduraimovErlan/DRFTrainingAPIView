from django.urls import path
from APIView6 import views


urlpatterns = [
    path('books6/', views.BookListView6.as_view()),
    path('books6/<int:pk>/', views.BookDetailView6.as_view()),
]