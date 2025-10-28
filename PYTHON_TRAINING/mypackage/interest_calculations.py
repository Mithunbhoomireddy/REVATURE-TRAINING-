"""
date: 28-10-2025
module for interest calculations
"""
def simple_interest(prin,ny,roi):
    """
    :param prin: principal amount
    :param ny:no of years
    :param roi: rate of interest
    :return:si,total amount
    """
    si=(prin*ny*roi)/100
    amount=prin+si
    return si,amount

def compound_interest(prin,t,roi):
    """
    :param prin:principal amount
    :param ny: no of years
    :param roi: rate of interest
    :return: si,total amount
    """
    amount=prin*((1+(roi/100))**(1*t))
    ci=amount-prin
    return ci,amount
