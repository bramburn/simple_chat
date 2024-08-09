from django.urls import path
from .views import UserList, UserDetail, UserCreate, UserUpdate

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/me/', UserDetail.as_view()),
    path('users/', UserCreate.as_view()),
    path('users/me/', UserUpdate.as_view()),
]