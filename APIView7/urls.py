from django.urls import path
from APIView7 import views


urlpatterns = [
    path('books7/', views.BookListView.as_view()),
    path('books7/<int:pk>/', views.BookDetail.as_view()),
]