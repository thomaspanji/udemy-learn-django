from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Learn Django"
    elif month == "february":
        challenge_text = "Do cycling"
    elif month == "march":
        challenge_text = "Walk for an hour"
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)