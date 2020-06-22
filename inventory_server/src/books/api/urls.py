from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view()),
    path('create', BookCreateView.as_view()),
    path('<pk>/update', BookUpdateView.as_view()),
    path('<pk>/delete', BookDeleteView.as_view()),
    path('<pk>', BookDetailView.as_view())
]