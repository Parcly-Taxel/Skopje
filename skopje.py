from constructs import *

def read_oscfiles(*fns):
    """Read oscillators and their minimum populations from provided files
    and return a dictionary."""
    res = {}
    for fn in fns:
        with open(fn, 'r') as f:
            for l in f:
                period, apgcode, mpop = l.split()
                period = int(period)
                res[period] = res.get(period, tuple()) + ((lt.pattern(apgcode), int(mpop)),)
    return res

def skop(p):
    """Return a list of pairs (Pattern, minimum population) representing
    the smallest known oscillators of the specified period."""
    fixed = read_oscfiles("fixedoscs")
    cands = list(fixed.get(p, []))
    cands.append(rectifier_loop(p))
    cands.append(mold_rectifier_loop(p))
    cands.append(p4_bumper_loop(p))
    cands.append(p8_loop(p))
    cands.append(snark_loop(p))
    cands.append(p6_bumper_loop(p))
    cands.append(pd_shuttle(p))
    cands.append(p6thumb_shuttle(p))
    cands.append(p14_shuttle(p))
    cands.append(twinbees_shuttle(p))
    cands = list(filter(bool, cands))
    if not cands:
        return []
    cands = [pair if pair[1] else (pair[0], minpop(pair[0])) for (i, pair) in enumerate(cands)]
    mp = min(pair[1] for pair in cands)
    return list(filter(lambda pair: pair[1] == mp, cands))
