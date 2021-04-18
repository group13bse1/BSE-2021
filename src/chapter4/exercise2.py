#define the function investment
def investiment(C, r, t, n ):
    #for simplicity we are going to do some calculations defferrently
    tn = t * n
    rn = r / n
    rn1 = 1 + rn
    rntn = rn1 ** rn
    p = C * rntn
    p = round(p, 2)
    return p