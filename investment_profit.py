import math


def get_profit_percentage(total_earnings_day, total_investments_captital):
    """
    Function to get the percentage to apply over the investments on the
    current day
    """
    if total_investments_captital is None or total_investments_captital == 0:
        raw_percentage_to_pay = 0
    else:
        raw_percentage_to_pay = (
            total_earnings_day / total_investments_captital
        ) * 100
    percentage_to_pay = 0
    if raw_percentage_to_pay >= 0.37:
        percentage_to_pay = 0.37
    elif raw_percentage_to_pay <= 0.28:
        percentage_to_pay = 0.28
    else:
        percentage_to_pay = math.floor(raw_percentage_to_pay * 100) / 100.0
    return percentage_to_pay


def get_profit_investment(total_investment_usd, percentage_to_apply):
    """
    Function to return the amount of xem to pay to a user by their investment
    """
    raw_value = (total_investment_usd * percentage_to_apply) / 100
    return math.floor(raw_value * 100) / 100.0