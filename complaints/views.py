from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaints
from .forms import ComplaintsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json
import urllib
from portal import settings
from .models import Complaints


def complaint_status(request):
    if request.method == 'GET':
        return render(request, 'complaint_status.html', {})
    else:
        ticket_id = request.POST.get('ticket_id')
        email = request.POST.get('email')
        try:
            filtered_complaint = Complaints.objects.get(ticket_id=ticket_id, email=email)
            return render(request, 'complaint_view.html', {'complaint': filtered_complaint})
        except:
            return render(request, 'complaint_status.html', {'message': 'Error'})

@login_required
def index(request):
    complaints = Complaints.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'complaints': complaints
    }
    return render(request, 'index.html', context)


@login_required
def details(request, id):
    complaint = Complaints.objects.get(id=id)

    context = {
        'complaint': complaint
    }

    return render(request, 'details.html', context)


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