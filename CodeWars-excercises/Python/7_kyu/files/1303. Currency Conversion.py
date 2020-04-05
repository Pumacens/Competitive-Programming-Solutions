def convert_my_dollars(usd, currency):
    if currency[0].lower() in set('aeiou'):
        return f"You now have {CONVERSION_RATES[currency] * usd } of {currency}."
        
    else:
        return f"You now have {int(str(CONVERSION_RATES[currency]) ,2) * usd} of {currency}." 



# def convert_my_dollars(usd, currency):
#     try:
#         amount = int(str(CONVERSION_RATES[currency]),2) * usd
#     except ValueError:
#         amount = CONVERSION_RATES[currency] * usd
    
#     return "You now have {} of {}.".format(amount, currency)