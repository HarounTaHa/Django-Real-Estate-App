from django.urls import path
from .views import RetrieveUserView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),
]
