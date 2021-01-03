from django.urls import path

from user.views  import KakaoSignUpView

urlpatterns = [
    path('/kakao-signup', KakaoSignUpView.as_view()),
]

