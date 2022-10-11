
from django.urls import path,include
from .views import UserViewset,RegisterUserAPIView,LoginUserAPIView
from rest_framework import routers
# from .views import
from rest_framework.authtoken import views

router=routers.DefaultRouter()
router.register(r'register',UserViewset)
# router.register(r'login',LoginUserAPIView)
urlpatterns = [
    path('',include(router.urls)),
    path('register',RegisterUserAPIView.as_view()),
    path('login',LoginUserAPIView.as_view()),
]