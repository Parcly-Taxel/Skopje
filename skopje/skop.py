from importlib import import_module
from lifelib.genera import sanirule

aliases = {"b3s23": "life"}

def minpop(pat):
    """Compute the minimum population of the given pattern.
    Because the latter is already associated with a rule no
    further arguments are required."""
    return min(pat[i].population for i in range(pat.period))

def skop(p, rule="b3s23"):
    """Return a list of pairs (Pattern, minimum population) representing
    the smallest known oscillators of the specified period in the given rule.
    Assumes that the local installation of lifelib knows about said rule."""
    rule = sanirule(rule)
    rmod = import_module(f"..{aliases.get(rule, rule)}", __name__)
    cands = []
    for line in rmod.fixeds.split("\n"):
        lp, apg, mp = line.split()
        if int(lp) == p:
            cands.append((rmod.lt.pattern(apg), int(mp)))
    for cfunc in rmod.cfuncs:
        cands.append(cfunc(p))
    cands = list(filter(bool, cands))
    if not cands:
        return []
    cands = [pair if pair[1] else (pair[0], minpop(pair[0])) for (i, pair) in enumerate(cands)]
    mp = min(pair[1] for pair in cands)
    return list(filter(lambda pair: pair[1] == mp, cands))
