from django.urls import path
from APIView import views

urlpatterns = [
    path('books1/', views.BookListView.as_view()),
    path('books1/<int:pk>/', views.BookDetailView.as_view()),
]
