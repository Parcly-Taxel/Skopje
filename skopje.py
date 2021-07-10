from constructs import *
fixed = {}

def skop(p):
    """Return a list of pairs (Pattern, minimum population) representing
    the smallest known oscillators of the specified period."""
    if not fixed:
        with open("fixedoscs", 'r') as f:
            for l in f:
                period, apgcode, mpop = l.split()
                period = int(period)
                fixed[period] = fixed.get(period, tuple()) + ((lt.pattern(apgcode), int(mpop)),)
    cands = list(fixed.get(p, []))
    cands.append(rectifier_loop(p))
    """
    cands = [construct_snark_loop(p),
             construct_p4_bumper_loop(p),
             construct_p8_loop(p),
             construct_p3_bumper_loop(p),
             construct_p6_bumper_loop(p),
             construct_p6thumb_shuttle(p),
             construct_pd0_shuttle(p),
             construct_pd15_shuttle(p),
             construct_pd30_shuttle(p),
             construct_pd45_shuttle(p),
             construct_pd60_shuttle(p),
             construct_pd75_shuttle(p),
             construct_pd90_shuttle(p),
             construct_tbs0_shuttle(p),
             construct_tbs138_shuttle(p)]"""
    cands = list(filter(bool, cands))
    if not cands:
        return []
    cands = [pair if pair[1] else (pair[0], minpop(pair[0])) for (i, pair) in enumerate(cands)]
    mp = min(pair[1] for pair in cands)
    return list(filter(lambda pair: pair[1] == mp, cands))
