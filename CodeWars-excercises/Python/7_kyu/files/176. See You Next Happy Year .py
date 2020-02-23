def next_happy_year(year):
    while True:
        year += 1
        if len(set(str(year))) == 4:
            break
            
    return year



# def next_happy_year(year):
    # return year + 1 if len(set(str(year + 1))) == 4 else next_happy_year(year + 1)