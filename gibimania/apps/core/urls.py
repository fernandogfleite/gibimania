from django.urls import path
from gibimania.apps.core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.do_login, name='login'),
    path('logout', views.do_logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
    path('turmajovem/', views.turmajovem, name='turmajovem'),
    path('turmacrianca/', views.turmacrianca, name='turmacrianca'),
]