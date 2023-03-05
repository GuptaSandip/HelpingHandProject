from django.contrib import admin
from django.urls import path
from home import views
from .views import login_view

urlpatterns = [
    path("",views.index, name='home'),
    path("test",views.test, name='test'),
    path("aptitude",views.aptitude, name='aptitude'),
    path("interview",views.interview, name='interview'),
    path("hrinter1",views.hrinter1, name='hrinter1'),
    path("hrinter2",views.hrinter2, name='hrinter2'),
    path("placement1",views.placement1, name='placement1'),
    path("placement2",views.placement2, name='placement2'),
    path("geneknow",views.geneknow, name='geneknow'),
    path("courses",views.courses, name='courses'),
    path("course1",views.course1, name='course1'),
    path("coursematerial",views.coursematerial, name='coursematerial'),
    path("logout",views.logoutUser, name='logout'),
    path("login",views.login_view, name='login'),
    path("register",views.register, name='register'),
    path("forget",views.forget, name='forget'),
    path("about",views.about, name='about'),
    path("logout",views.logoutUser, name='logout')
]

