from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaints
from .forms import ComplaintsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json


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
        response = {}
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            response['status'] = True
            response['message'] = 'Successfully Created!'
            form.save()
        else:
            print(form)
            print('Error | ', form.errors.as_json())
            response['status'] = False
            error_message = ''
            json_error = json.loads(form.errors.as_json())
            # TODO: Check for multiple error
            for error in json_error:
                print(json_error)
                error_message += json_error[error][0]['message']
                error_message += '\n'
            print('message = ', error_message)
            response['message'] = error_message

        data = json.dumps(response)
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