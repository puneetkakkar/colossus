from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import form_signup, form_login
from django.contrib.auth.models import User
from home_and_login.models import user_details
import random


def home_page(request):
    user_id_in_action = request.user.id
    if user_id_in_action is not None:
        fetched_data = user_details.objects.filter(user_id=user_id_in_action).values_list('profile_link')
        print(fetched_data[0][0])
        return render(request, 'home_and_login/home_page_driver.html',
                  {'profile_link': fetched_data[0][0]})
    else:
        return render(request, 'home_and_login/home_page_driver.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("User is valid, active and authenticated")
                return HttpResponse("Logged in")
            else:
                print(
                    "The password is valid, but the account has been disabled!")
        else:
            print("The username and password were incorrect.")
            return HttpResponse("Sorry, check initials")


def logout_user(request):
    logout(request)
    return home_page(request)

def add_new_user(request):
    print('hello')
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        # email is also username,
        user = User.objects.create_user(
            email, email, password)
        # split full name and save
        full_name = full_name.split()
        if len(full_name) == 1:
            user.first_name = full_name[0]
        else:
            user.last_name = full_name[-1]
            user.first_name = " ".join(full_name[:-1])
        # unique profile link
        one_word_first_name = user.first_name.split(' ')
        user_profile_hash = one_word_first_name[
            0].lower() + str(random.randrange(1000, 9999))
        full_name = ' '.join(full_name)
        user_details_save = user_details.objects.create(
            user=user, full_name=full_name, profile_link=user_profile_hash)
        user.save()
        # send email from here
    return login_user(request)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/home/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home_and_login/setting.html', {
        'form': form
    })
