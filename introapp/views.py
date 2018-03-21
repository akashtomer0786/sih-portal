from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'home.html', {})


def types_of_cb(request):
    return render(request, 'typesofbullying.html', {})


def type_trolling(request):
    return render(request, 'trolling.html', {})


def type_trickery(request):
    return render(request, 'trickery.html', {})


def type_outing(request):
    return render(request, 'outing.html', {})


def type_harrassment(request):
    return render(request, 'harrassment.html', {})


def type_frapping(request):
    return render(request, 'frapping.html', {})


def type_fakeprofile(request):
    return render(request, 'fakeprofile.html', {})


def type_exclusion(request):
    return render(request, 'exclusion.html', {})


def type_cyberstalking(request):
    return render(request, 'cyberstalking.html', {})


def type_catphishing(request):
    return render(request, 'catphishing.html', {})