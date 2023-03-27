from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Jan: stay warm",
    "february": "Feb: walk everyday",
    "march": "March: get new wardrobe",
    "april": "April: get warm",
    "may": "May: take pictures",
    "june": "June: play volleyball",
    "july": "July: stay cool",
    "august": "August: rest",
    "september": "Sept: go to Paris",
    "october": "Oct: get a new job",
    "november": "Nov: stay happy",
    "december": "Dec: not get depressed",
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # for exmaple: /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
