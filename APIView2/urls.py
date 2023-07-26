from django.urls import path
from APIView import views

urlpatterns = [
    path('books2/', views.BookListView.as_view()),
    path('books2/<int:pk>/', views.BookDetailView.as_view()),
]