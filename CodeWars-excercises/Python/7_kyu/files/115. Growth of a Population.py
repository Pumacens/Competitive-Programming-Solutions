def nb_year(p0, percent, aug, p):
    pop = p0
    year = 0
    while pop < p:
        pop = pop*(1+ (percent/100)) + aug
        year += 1
        
    return year



from math import ceil, log
def nb_year(p0, percent, aug, p):
    if not percent: return ceil(1.*(p - p0) / aug)
    percent = 1 + percent / 100.
    r = aug / (1 - percent)
    return ceil(log((p - r) / (p0 - r), percent))



'''
Basically, the formula of year n's population is p0*(1-percent)^n+aug*[(1+percent)^(n-1)+(1+percent)^(n-2)+...+1], 
which is also equal to p0*(1-percent)^n+aug*[(1+percent)^n-1]/percent, then p0*(1-percent)^n+aug/percent*(1+percent)^n-aug/percent 
and finaly (p0+aug/percent)*(1+percent)^n-aug/percent.
By solving p = (p0+aug/percent)*(1+percent)^n-aug/percent for n, we can get n = log( (p+aug/percent)/(p0+aug/percent), 1+percent).

In lechevalier's solution, his percent is actually 1+percent and his r is -aug/percent, so his last line became log((p-r)/(p0-r), percent).

'''