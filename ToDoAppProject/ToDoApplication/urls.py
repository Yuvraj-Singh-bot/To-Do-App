from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.signup),
    path('signup/', views.signup),
    path('login/', views.loginFunction),
    path('todopage', views.todo),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('signout/', views.signout, name='signout'),
    
]