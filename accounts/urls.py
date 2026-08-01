from django.urls import path
from .views import SignUpView, add_funds

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('add-funds/', add_funds, name='add_funds'),
]
