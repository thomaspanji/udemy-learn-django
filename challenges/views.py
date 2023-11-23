from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat healthy food",
    "february": "Walk for 20 minutes",
    "march": "Learn Django",
    "april": "Do cycling",
    "may": "Do exercise",
    "june": "Relax brother",
    "july": "Eat healthy food",
    "august": "Walk for 20 minutes",
    "september": "Learn Django",
    "october": "Do cycling",
    "november": "Do exercise",
    "december": "Relax brother",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month number")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Invalid month!")