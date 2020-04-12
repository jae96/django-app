import math


def estimator(data):

    # Challenge 1
    reportedCases = data["reportedCases"]

    impact = {"currentlyInfected": float(reportedCases * 10)}
    severeImpact = {"currentlyInfected": float(reportedCases * 50)}

    # Calculate infectionsByRequestedTime by finding the find the period type and timeToElapse and calculate factor
    timeToElapse = data["timeToElapse"]
    periodType = data["periodType"]
    if periodType == "days":
        finalTimeToElapse = timeToElapse
    if periodType == "weeks":
        finalTimeToElapse = timeToElapse * 7  # There are seven days in a week
    if periodType == "months":
        finalTimeToElapse = timeToElapse * 30  # Assuming 30 days in a month

    factor = math.floor(finalTimeToElapse / 3)

    impact["infectionsByRequestedTime"] = float(impact["currentlyInfected"] * (2 ** factor))
    severeImpact["infectionsByRequestedTime"] = float(severeImpact["currentlyInfected"] * (2 ** factor))

    # Challenge 2
    impact["severeCasesByRequestedTime"] = float(impact["infectionsByRequestedTime"] * 0.15)
    severeImpact["severeCasesByRequestedTime"] = float(severeImpact["infectionsByRequestedTime"] * 0.15)

    totalHospitalBeds = data["totalHospitalBeds"]

    hospitalBedsByRequestedTime = (0.35 * totalHospitalBeds) - impact[
        "severeCasesByRequestedTime"]
    if hospitalBedsByRequestedTime >= 0:
        impact["hospitalBedsByRequestedTime"] = float(math.floor(hospitalBedsByRequestedTime))
    else:
        impact["hospitalBedsByRequestedTime"] = float(math.ceil(hospitalBedsByRequestedTime))

    hospitalBedsByRequestedTime = (0.35 * totalHospitalBeds) - severeImpact[
        "severeCasesByRequestedTime"]
    if hospitalBedsByRequestedTime >= 0:
        severeImpact["hospitalBedsByRequestedTime"] = float(math.floor(hospitalBedsByRequestedTime))
    else:
        severeImpact["hospitalBedsByRequestedTime"] = float(math.ceil(hospitalBedsByRequestedTime))

    # Challenge 3
    impact["casesForICUByRequestedTime"] = float(math.floor(impact["infectionsByRequestedTime"] * 0.05))
    severeImpact["casesForICUByRequestedTime"] = float(math.floor(severeImpact["infectionsByRequestedTime"] * 0.05))

    impact["casesForVentilatorsByRequestedTime"] = float(math.floor(impact["infectionsByRequestedTime"] * 0.02))
    severeImpact["casesForVentilatorsByRequestedTime"] = float(math.floor(severeImpact["infectionsByRequestedTime"] * 0.02))

    region = data["region"]  # Get the region
    avgDailyIncomeInUSD = region["avgDailyIncomeInUSD"]
    avgDailyIncomePopulation = region["avgDailyIncomePopulation"]


    impact["dollarsInFlight"] = float(math.floor((impact["infectionsByRequestedTime"] *
                                                  avgDailyIncomePopulation * avgDailyIncomeInUSD) / finalTimeToElapse))
    severeImpact["dollarsInFlight"] = float(math.floor((severeImpact["infectionsByRequestedTime"] *
                                                       avgDailyIncomePopulation * avgDailyIncomeInUSD) / finalTimeToElapse))

    data = {"impact": impact, "severeImpact": severeImpact}

    return data
