from django.urls import path
from .views import UserCreate, CustomTokenObtainPairView, WordListCreate, WordRetrieveUpdateDestroy, UserWordProgressListCreate, UserWordProgressRetrieveUpdateDestroy

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('words/', WordListCreate.as_view(), name='word-list-create'),
    path('words/<int:pk>/', WordRetrieveUpdateDestroy.as_view(), name='word-retrieve-update-destroy'),
    path('user-word-progress/', UserWordProgressListCreate.as_view(), name='user-word-progress-list-create'),
    path('user-word-progress/<int:pk>/', UserWordProgressRetrieveUpdateDestroy.as_view(), name='user-word-progress-retrieve-update-destroy'),
]