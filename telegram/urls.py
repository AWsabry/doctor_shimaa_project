from django.urls import path
from . import views


app_name = 'telegram_app'

urlpatterns = [
    # URL pattern with channel username and user ID as parameters
    path('messages/<str:channel_username>/', views.get_user_messages, name='get_user_messages'),
    path('get_articles/', view= views.get_articles.as_view(), name='get_articles'),
    path('get_categories/', view= views.get_categories.as_view(), name='get_categories'),

]