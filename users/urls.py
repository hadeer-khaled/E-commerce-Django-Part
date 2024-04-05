from .views import UserView , UserLogin , UserRegister , UserLogout , AdminLogin
from django.urls import path
from .views import UserView , OneUserView

urlpatterns = [
    path('', UserView.as_view()),
    path('user/<int:user_id>',OneUserView.as_view()),
    path('login/', UserLogin.as_view() ),
    path('register/', UserRegister.as_view()),
    path('logout/', UserLogout.as_view()),
    path('admin/login/', AdminLogin.as_view() ),
]