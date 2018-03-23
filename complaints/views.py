from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComplaintsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
import urllib
from portal import settings
from .models import Complaints
from django.core.mail import send_mail
import hashlib


# TODO: Change email to lowercase and then filter it out
# TODO: Change complaint view for user side
# TODO: Forgot Ticket ID
def complaint_status(request):
    if request.method == 'GET':
        return render(request, 'complaint_status.html', {})
    else:
        ticket_id = request.POST.get('ticket_id')
        email = request.POST.get('email').lower()
        try:
            filtered_complaint = Complaints.objects.get(ticket_id=ticket_id, email=email)
            return render(request, 'complaint_view.html', {'complaint': filtered_complaint})
        except:
            return render(request, 'complaint_status.html', {'message': 'Error'})


@login_required
def index(request):
    complaints = Complaints.objects.filter(mail_confirm=True)[:10]

    context = {
        'title': 'Latest Posts',
        'complaints': complaints
    }
    return render(request, 'index.html', context)


# TODO: Option to assign complaint to any particular official
# TODO: Show official name who have been assigned for it
@login_required
def details(request, id):
    complaint = Complaints.objects.get(id=id)

    context = {
        'complaint': complaint
    }

    return render(request, 'details.html', context)


# TODO: Recheck the complaint_Tag with given predefined tags from python
def ajax_form(request):
    print('I CAME HERE')
    if request.method == 'POST':
        response_data = {}
        form = ComplaintsForm(request.POST)
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
                response_data['status'] = True
                response_data['message'] = 'Successfully Created!'
                form.save()
                filtered_complaint = Complaints.objects.get(email=request.POST.get('email'),
                                                            complaint=request.POST.get('complaint'))
                print(filtered_complaint)
                print(filtered_complaint.ticket_id)

                confirmation_link = hashlib.md5((filtered_complaint.email + filtered_complaint.ticket_id).encode('utf-8')).hexdigest()
                filtered_complaint.key = confirmation_link
                filtered_complaint.save()
                mail_subject = 'Details about your Request'
                mail_message = 'Hi\nPlease note down these details as it will help you' \
                               '\nName: ' + filtered_complaint.full_name + '' \
                               '\nPhone Number: ' + filtered_complaint.phone_number + '' \
                               '\nSubject: ' + filtered_complaint.subject + '' \
                               '\nTicket Id: ' + filtered_complaint.ticket_id + '' \
                               '\nFor status on your report use your ticket Id and Email' \
                               '\n\nClick here to confirm your registration' \
                               '\nhttp://127.0.0.1:8000/complaints/form/confirm/' + confirmation_link + '' \
                               '\nThank you'
                print(mail_message)
                send_mail(
                    mail_subject,
                    mail_message,
                    'shashank.sharma98@gmail.com',
                    [filtered_complaint.email],
                    fail_silently=False,
                )
            else:
                response_data = {
                    'status': True,
                    'message': 'Captcha Error',
                }
        else:
            print(form)
            print('Error | ', form.errors.as_json())
            response_data['status'] = False
            error_message = ''
            json_error = json.loads(form.errors.as_json())
            # TODO: Check for multiple error
            for error in json_error:
                print(json_error)
                error_message += json_error[error][0]['message']
                error_message += '\n'
            print('message = ', error_message)
            response_data['message'] = error_message

        data = json.dumps(response_data)
        return HttpResponse(data, content_type='application/json')
    else:
        return redirect('complaints')


def complaint_form(request):
    if request.method == 'GET':
        form = ComplaintsForm
        return render(request, 'complaint_form.html', {'form': form})


def success(request):
    if request.method == 'GET':
        return render(request, 'success_form.html')


def activate_complaint(request, key):
    print('I got KEY | ', key)
    try:
        filtered_complaint = Complaints.objects.get(key=key)
        filtered_complaint.mail_confirm = True
        filtered_complaint.save()
        return render(request, 'success_form.html', {})
    except:
        return render(request, 'wrong.html', {})