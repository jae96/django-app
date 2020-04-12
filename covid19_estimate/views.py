from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import sys
sys.path
from estimator import estimator

def home(request):
    return render(request, 'home.html', {'name': 'Abel'})


def estimate(request):

    population = float(request.GET["data-population"])
    timeToElapse = float(request.GET["data-time-to-elapse"])
    reportedCases = float(request.GET["data-reported-cases"])
    totalHospitalBeds = float(request.GET["data-total-hospital-beds"])
    periodType = request.GET["data-period-type"]

    input = {"region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 4,
        "avgDailyIncomePopulation": 0.73
    }, "periodType": periodType,
        "timeToElapse": timeToElapse,
        "reportedCases": reportedCases,
        "population": population,
        "totalHospitalBeds": totalHospitalBeds}

    estimate = estimator(input)
    impact = estimate['impact']
    severeImpact = estimate['severeImpact']

    impact_dollarsInFlight = impact["dollarsInFlight"]
    severeImpact_dollarsInFlight = severeImpact["dollarsInFlight"]


    return render(request, 'results.html', {'impact_dollarsInFlight': impact_dollarsInFlight,
                                            'severeImpact_dollarsInFlight': severeImpact_dollarsInFlight})
