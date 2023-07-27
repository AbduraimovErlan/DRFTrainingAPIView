from django.urls import path
from APIView8 import views

urlpatterns = [
    path('books8/', views.BookListView.as_view()),
    path('books8/<int:pk>/', views.BookDetail.as_view()),
]