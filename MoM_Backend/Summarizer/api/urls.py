from django.urls import path
from .views import apiOverview, getMeet, createMeet, translateText, bartSummarizer, nltkSummarizer
from .views import current_user, UserList

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('apiOverview',apiOverview),
    path('createMeet', createMeet),
    path('getMeet', getMeet),
    path('translateText', translateText),
    path('bartSummarizer', bartSummarizer),
    path('nltkSummarizer', nltkSummarizer),
]