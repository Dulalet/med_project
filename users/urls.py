from django.urls import path
from .views import AuthViewSet

urlpatterns = [
    path('login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('register/', AuthViewSet.as_view({'post': 'register'}), name='register'),
    path('logout/', AuthViewSet.as_view({'post': 'logout'}), name='logout'),
    path('getUser/', AuthViewSet.as_view({'get': 'get_user'}), name='getuser'),
    path('password_change/', AuthViewSet.as_view({'post': 'password_change'}), name='changepass'),
]