from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from complaints.models import Complaints
import datetime


# Dashboard for /analytics/dashboard to view data
@login_required()
def dashboard(request):
    return render(request, 'analytics_home.html', {})


###################################################
#                                                 #
#                                                 #
#                       API                       #
#                                                 #
#                                                 #
###################################################


# TODO: Filter date and make use of +05:30
def compare_date(date_one, date_two):
    """
    Compare date, time and return boolean value
    :param date_one: Date in format: 2018-03-23 18:40:53.731846 +05:30
    :param date_two: Date in format: 2018-03-23 18:40:53.731846 +05:30
    :return:
    """
    pass


# TODO: Compare each string with given set and then only show result
# TODO: Performance issue while creating new list
# TODO: Make sure of State Codes
# TODO: Make use of Tags
@api_view(['GET'])
def get_complaints(request):
    get_gender = request.GET.get('gender')
    get_state = request.GET.get('state')
    get_city = request.GET.get('city')
    get_complaints_from = request.GET.get('from')
    get_complaints_to = request.GET.get('to')
    if get_complaints_from == get_complaints_to and not get_complaints_from:
        get_complaints_range = None
    else:
        if get_complaints_from:
            get_complaints_range = [get_complaints_from, str(datetime.datetime.now().date()) + ' 23:59:59']
        else:
            get_complaints_range = ['2017-01-01', get_complaints_to]

    print(get_complaints_range)

    # TODO: Comma seperated values can be seperated
    gender_list = {
        'male': 'M',
        'female': 'F',
        'others': 'O'
    }

    # Check if all parameters passed is correct or not
    gender = gender_list[get_gender.lower()] if get_gender and get_gender.lower() in gender_list else None

    complaint_list = Complaints.objects.myfilter(gender=gender,
                                                 state__iexact=get_state,
                                                 city__iexact=get_city,
                                                 complaint_date__range=get_complaints_range)
    data = {
        'complaints': len(complaint_list),
        'subject_list': [subject.subject for subject in complaint_list]
    }
    return Response(data)