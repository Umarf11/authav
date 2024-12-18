from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserPasswordView, UserSendResetPasswordEmailView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="user-profile"),
    path('changepass/', UserPasswordView.as_view(), name="chnagepassword"),
    path('check-reset-email-link/', UserSendResetPasswordEmailView.as_view(), name="resetpass"),

]
