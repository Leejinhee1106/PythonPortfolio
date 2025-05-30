from django.urls import path

from .import views

urlpatterns = [
    path('',views.main, name='main'),
    path('members/',views.members, name='members'),
    path('details/',views.members, name='details'),
    path('syntax/',views.syntax, name='syntax'),
    path('ifelse/',views.ifelse, name='ifelse'),
    path('forloop/', views.forloop, name='forloop'),
] #멤버즈라는 url을 만들어 준 것. 거기에 views에 쓴 내용을 담아온다