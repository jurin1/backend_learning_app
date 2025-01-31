from django.urls import path
from .views import UserCreate, CustomTokenObtainPairView

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]