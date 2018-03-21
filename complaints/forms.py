from django import forms
from django.core.validators import RegexValidator
from portal import settings

from .models import Complaints

class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        # TODO: FIX DateOfBirth default input format to dd/mm/yyyy
        # date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        fields = ['full_name',
                  'gender',
                  'date_of_birth',
                  'phone_number',
                  'email',
                  'state',
                  'city',
                  'subject',
                  'complaint',
                  'complaint_against',
                  'complaint_tag']

    def __init__(self, *args, **kwargs):
        super(ComplaintsForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs \
            .update({
                'class': 'datepicker',
            })
        self.fields['complaint'].widget.attrs \
            .update({
                'class': 'materialize-textarea',
            })
        # self.fields['complaint_tag'].widget.attrs \
        #     .update({
        #         'disabled': '',
        #     })
    # full_name = forms.CharField(max_length=200)
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Others'),
    # )
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select())
    # date_of_birth = forms.DateField(widget=forms.SelectDateWidget())
    # phone_number = forms.CharField(validators=[phone_regex], max_length=15)
    # email = forms.EmailField()
    # state = forms.CharField(max_length=60)
    # city = forms.CharField(max_length=60)
    # subject = forms.CharField(max_length=140)
    # complaint = forms.CharField()
    # complaint_against = forms.CharField(max_length=200)
    # complaint_tag = forms.CharField(max_length=200)
    #
    # def save(self, request):
    #     user = super(ComplaintsForm, self).save(request)
    #     try:
    #         data = self.cleaned_data
    #         complaints = Complaints(full_name=data.get('full_name'),
    #                                 gender=data.get('gender'),
    #                                 date_of_birth=data.get('date_of_birth'),
    #                                 phone_number=data.get('phone_number'),
    #                                 email=data.get('email'),
    #                                 state=data.get('state'),
    #                                 city=data.get('city'),
    #                                 subject=data.get('subject'),
    #                                 complaint=data.get('complaint'),
    #                                 complaint_against=data.get('complaint_against'),
    #                                 complaint_tag=data.get('complaint_tag'))
    #         complaints.save()
    #         return user
    #
    #     except:
    #         print('ERROR')