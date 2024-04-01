from .views import UserView
from django.urls import path
from .views import UserView , OneUserView
urlpatterns = [
    path('', UserView.as_view()),
    path('user/<int:user_id>/', OneUserView.as_view()),]