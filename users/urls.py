from .views import UserView , UserLogin , UserRegister , UserLogout
from django.urls import path
urlpatterns = [
    path('', UserView.as_view()),
    path('login/', UserLogin.as_view() ),
    path('register/', UserRegister.as_view()),
    path('logout/', UserLogout.as_view()),
]