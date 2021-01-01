from django.urls import path

from user.views  import SignUpView, SignInView, PasswordChangeView, PasswordCheckView, PhonenumberChangeView


urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/password/change', PasswordChangeView.as_view()),
    path('/password/check', PasswordCheckView.as_view()),
    path('/phonenumber/change', PhonenumberChangeView.as_view()),
]

