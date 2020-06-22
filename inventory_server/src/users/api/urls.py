from django.urls import path
from .views import UserListView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view()),
    path('create', UserCreateView.as_view()),
    path('<pk>', UserDetailView.as_view())
]