"""views of django"""
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import Profile, Univer_Profile, Club_Profile, Open_Position_for_Un
from .models import Achivment, Extra_Languages, Teem

from .forms import UserForm, Un_ProfileForm, Cl_ProfileForm, Un_Position_Form
from .forms import user_main_form, user_letter_form
from .forms import User_Lang_Form, User_Ach_Form, User_Teem_Form


def menu_user():
    """menu for user"""
    return [
        {'link': "/University", 'name': 'Университеты'},
        # {'link': "/Сlubs", 'name': 'Клубы'},
        {'link': "/Positions/?owner=", 'name': 'Позиции'},
        {'link': "/accounts/prof/", 'name': 'Профиль'},
        {'link': "/accounts/logout/", 'name': 'Выход'},
    ]


def menu_anther():
    """menu for ather"""
    return [
        {'link': "/Athletes", 'name': 'Спортсмены'},
        {'link': "/accounts/prof_un/", 'name': 'Профиль'},
        {'link': "/accounts/logout/", 'name': 'Выход'},
    ]


def web():
    """social"""
    return [
        {
            # facebook
            'link': 'https://www.facebook.com/Teamed-Up-363186321537325',
            'class': 'feather feather-facebook fea icon-sm fea-social',
            'path': 'M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z',
            'x': '-1000',
            'y': '-1000',
            'width': '-1000',
            'height': '-1000',
            'rx': '-1000',
            'ry': '-1000',
            'x1': '-1000',
            'y1': '-1000',
            'x2': '-1000',
            'y2': '-1000',
            'cx': '-1000',
            'cy': '-1000',
            'r': '-1000',
        },
        {
            # instagram
            'link': 'https://www.instagram.com/teamedup_recruitment/ ',
            'class': "feather feather-instagram fea icon-sm fea-social",
            'path': "M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z",
            'x': '2',
            'y': '2',
            'width': '20',
            'height': '20',
            'rx': '5',
            'ry': '5',
            'x1': '17.5',
            'y1': '6.5',
            'x2': '17.51',
            'y2': '6.5',
            'cx': '',
            'cy': '',
            'r': '',
        },

    ]


def company():
    """info for connect"""
    return [
        {
            'link': '',
            'name': ' About us'
        },
        {
            'link': '',
            'name': ' Services'
        },
        {
            'link': '',
            'name': ' Team'
        },
        {
            'link': '',
            'name': ' Pricing'
        },
        {
            'link': '',
            'name': ' Project'
        },
        {
            'link': '',
            'name': ' Careers'
        },
        {
            'link': '',
            'name': ' Blog'
        },
        {
            'link': '',
            'name': ' Login'
        },
    ]


def usfull_links():
    """info for move"""
    return [
        {
            'link': '/',
            'name': 'For sportmen'
        },
        {
            'link': '/start_un/',
            'name': 'For university'
        },
        # {'link': '/start_cl/','name': 'For club'},
        {
            'link': '',
            'name': 'Privacy Policy'
        },
        {
            'link': '',
            'name': 'Documentation'
        },
        {
            'link': '',
            'name': 'Changelog'
        },
        {
            'link': '',
            'name': 'Components'
        },
    ]


def user_dop_content():
    """main info for user"""
    return {
        'menu_user': menu_user(),
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
    }


def ather_dop_content():
    """main info for ather"""
    return {
        'menu_ather': menu_anther(),
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
    }


def start_user_link():
    """Info for start page"""
    return {
        'name': 'sportmen',
        'reg': '/accounts/login/',
        'enter': '/accounts/reg/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),
    }


def start_un_link():
    """Info for start page"""
    return {
        'name': 'university',
        'reg': '/accounts/login_Un/',
        'enter': '/accounts/reg_un/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),

    }


def start_cl_link():
    """Info for start page"""
    return {
        'name': 'clubs',
        'reg': '/accounts/login_Cl/',
        'enter': '/accounts/reg_cl/',
        'web': web(),
        'company': company(),
        'usfull_links': usfull_links(),

    }


def start_user(request):
    """first page for user"""
    data = start_user_link()
    return render(request, 'start.html', data)


def create_user_profile(biscuits):
    """create profile """
    Profile.objects.create(biscuits=biscuits)


@transaction.atomic
def update_profile_user(request):
    """ update profile user """
    temp = None
    data = {}
    #t=request.COOKIES['csrftoken']
    #if len(Profile.objects.filter(biscuits=t))==0:
    #    create_user_profile(t)
    if request.method == 'POST':
        user_form = user_main_form(request.POST)

        flag = True


        if user_form.is_valid() and flag:
            #            Profile.objects.filter(id=request.user.profile.id).update(user_flag=True)
            #temp = request.user.profile
            #temp.user_flag = True
            #temp.save()
            print("\n:)\n")
            user_form.save()
            # messages.success(request, ('Ваш профиль был успешно обновлен!'))
        else:
            data['error2'] = '2'

            data['user_form'] = user_form
            flag = False


        if flag:
            return redirect('start_user')
        return render(request, 'accounts/prof_set.html', data)

    user_form = user_main_form()


    data['user_form'] = user_form


    return render(request, 'accounts/prof_set.html', data)


@login_required
@transaction.atomic
def update_letter(request):
    """ update letter """

    data = {}
    if request.method == 'POST':
        letter_form = user_letter_form(request.POST, instance=request.user.profile)

        flag = True

        if letter_form.is_valid():
            letter_form.save()
        else:
            data['error'] = '1'

            data['letter_form'] = letter_form
            flag = False

        if flag:
            return redirect('profile')

        return render(request, '/accounts/prof_letter.html', data)

    letter_form = user_letter_form(instance=request.user.profile)

    data['letter_form'] = letter_form

    return render(request, 'accounts/prof_letter.html', data)