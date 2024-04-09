from .views import UserView , UserLogin , UserRegister , UserLogout , AdminLogin
from django.urls import path
from .views import UserView , OneUserView , OneUserOrdersView
from order_item.views import  OrderItemDetailView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', UserView.as_view()),
    path('user/<int:user_id>/',OneUserView.as_view()),
    path('user/<int:user_id>/orders/',OneUserOrdersView.as_view()),
    path('user/orders/order/<int:order_id>/',OrderItemDetailView.as_view()),
    path('login/', UserLogin.as_view() ),
    path('register/', UserRegister.as_view()),
    path('logout/', UserLogout.as_view()),
    path('admin/login/', AdminLogin.as_view() ),
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)