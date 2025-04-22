from django import template
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter(name="multiply")
def multiply(value, arg):
    return Decimal(str(value)) * Decimal(str(arg))

@register.filter(name="divide")
def divide(value, arg):
    return Decimal(str(value)) / Decimal(str(arg))
    
def add_interest(value, interest_rate):
    try:
        principal = Decimal(str(value))
        annual_interest_rate = Decimal(str(interest_rate))

        interest = principal * (annual_interest_rate / 100)
        
        return round(interest, 2)
    
    except (ValueError, TypeError, Decimal.InvalidOperation) as e:
        logger.error("Error adding interest", exc_info=True)
        return 0.0

@register.simple_tag
def calculate_monthly_payment(loan_amount, args):
    if loan_amount is None or loan_amount == 0:
        return 0.0
    try:
        if isinstance(args, (list, tuple)):
            interest_rate, years = args
        elif isinstance(args, str):
            interest_rate, years = args.split(',')
        else:
            interest_rate, years = args, 5
        
        interest_rate = Decimal(str(interest_rate)) / 100
        monthly_rate = interest_rate / 12

        total_payments = int(years) * 12

        if monthly_rate == 0:
            monthly_payment = Decimal(str(loan_amount)) / total_payments
        else:
            numerator = monthly_rate * (1 + monthly_rate) ** total_payments
            denominator = (1 + monthly_rate) ** total_payments - 1
            if denominator != 0:
                monthly_payment = Decimal(str(loan_amount)) * (numerator / denominator)
            else:
                monthly_payment = Decimal(str(loan_amount)) / total_payments

        return monthly_payment
    except (ValueError, TypeError, AttributeError):
        logger.error("Error calculating monthly payment", exc_info=True)
        return 0.0

@register.simple_tag
def calculate_hpp(base_price, loan, interest_rate, cost_service):
    try:
        base_price = float(base_price) if base_price else 0.0
        loan = float(loan) if loan else 0.0
        interest_rate = float(interest_rate) if interest_rate else 0.0
        cost_service = float(cost_service) if cost_service else 0.0

        interest = loan * (interest_rate / 100)

        hpp = base_price + interest + cost_service

        return max(hpp, 0.0)
    except (ValueError, TypeError):
        logger.error("Error calculating HPP", exc_info=True)
        return 0.0