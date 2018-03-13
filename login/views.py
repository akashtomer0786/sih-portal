from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.db import transaction
from django.conf import settings
from django.contrib import messages

from login.forms import SignUpForm, UserForm, ProfileForm, PhoneDetailsForm
from login.tokens import account_activation_token

import json
import urllib


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = PhoneDetailsForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                print("Success")
                form.save()

                phone = form2.save(commit=False)
                phone.username = form.cleaned_data['username']
                phone.save()

                user = form.save(commit=False)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)

                return redirect('account_activation_sent')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.', extra_tags='safe')
    else:
        form = SignUpForm()
        form2 = PhoneDetailsForm()
    return render(request, 'signup.html', {'form': form, 'form2': form2})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('success')
    else:
        return render(request, 'account_activation_invalid.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        signup_form = SignUpForm(instance=request.user)
        print(signup_form)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
        else:
            return render(request, 'settings.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'signup_form': signup_form,
        })
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        signup_form = SignUpForm(instance=request.user)
        print('This is what you got')
        print(signup_form)
    return render(request, 'settings.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'signup_form': signup_form,
    })
