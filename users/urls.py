from django.urls import path,include

from . import views

urlpatterns = [
    path("register", views.register_page, name="register"),
    path('login',views.login_user,name ="login"),
    path('logout',views.logout_page,name='logout'),
    path("blog/",include("blog.urls"))

]