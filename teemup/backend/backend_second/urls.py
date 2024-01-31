"""backend_second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from TeamedUp import views

from TeamedUp.views import *

urlpatterns = [
    # accounts/logout/
    path('admin/', admin.site.urls),

    # path('accounts/', include('django.contrib.auth.urls')),

    path("University/", views.uni),
    #path("Сlubs/", views.clubs),
    path("Athletes/", views.sports),
    path("Resume/", views.sports),
    path("Positions/", views.pos),

    path("Athletes/resume/", views.show_res, name='show_resume'),

    path('accounts/logout/', views.login_out, name="logout"),

    path('accounts/login/', login_view_user.as_view(), name="login"),
    path('accounts/login_Un/', login_view_univer.as_view(), name="login_un"),
    path('accounts/login_Cl/', login_view_club.as_view(), name="login_cl"),

    path('', views.start_user, name="start_user"),
    path('start_un/', views.start_un, name="start_un"),
    path('start_cl/', views.start_cl, name="start_cl"),

    path('accounts/prof/', profile_page_user.as_view(), name="profile"),
    path('accounts/prof_un/', profile_page_univer.as_view(), name="un_profile"),
    path('accounts/prof_cl/', profile_page_club.as_view(), name="cl_profile"),

    path('accounts/reg/', register_view_user.as_view(), name="register"),
    path('accounts/reg_un/', register_view_univer.as_view(), name="register_un"),
    path('accounts/reg_cl/', register_view_club.as_view(), name="register_cl"),

    # path('/accounts/change_pas', 'django.contrib.auth.views.password_change', name='password_change'),
    #accounts/prof_set/
    path('accounts/prof/accounts/prof_set/', views.update_profile_user, name='setting'),
    path('accounts/prof/accounts/bio_set/', views.set_bio_user, name='setting_bio'),
    path('accounts/prof/accounts/academy_set/', views.set_acd_user, name='setting_acd'),
    path('accounts/prof/accounts/sport_set/', views.set_sport_user, name='setting_sport'),

    path('accounts/prof/accounts/letter/', views.update_letter, name='letter'),

    path('accounts/prof/accounts/lan/', views.create_lang_user, name='add_lan'),
    path('accounts/prof/accounts/lan_set/', views.set_lang_user, name='lan_set'),
    path('accounts/prof/accounts/lan/delete/', views.delete_lan, name='lan_delete'),

    path('accounts/prof/accounts/ach/', views.create_ach_user, name='add_ach'),
    path('accounts/prof/accounts/ach_set/', views.set_ach_user, name='ach_set'),
    path('accounts/prof/accounts/ach/delete/', views.delete_ach, name='ach_delete'),

    path('accounts/prof/accounts/teem/', views.create_teem_user, name='add_teem'),
    path('accounts/prof/accounts/teem_set/', views.set_teem_user, name='teem_set'),
    path('accounts/prof/accounts/teem/delete/', views.delete_teem, name='teem_delete'),

    path('accounts/prof_set_un/', views.update_profile_univer, name='setting_un'),
    path('accounts/prof_set_cl/', views.update_profile_club, name='setting_cl'),

    path('accounts/position_un/', views.create_position_univer, name='pos_un'),
    path('accounts/position_cl/', views.create_position_club, name='pos_cl'),

    path('accounts/prof_un/position_un_set/', views.set_position_univer, name='pos_un_set'),
    #path('accounts/position_cl_set/', views.set_position_cl, name='pos_cl_set'),
    path('accounts/prof_un/position_un_set/delete/', views.delete_pos, name='pos_un_set_delete'),
    #path('accounts/prof_un/position_cl_set/delete', views.set_position_un, name='pos_cl_set_delete'),

    #path('accounts/position_cl/', views.update_profile_cl, name='pos_cl'),
]
