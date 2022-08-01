from importlib import import_module
from lifelib.genera import sanirule

aliases = {"b3s23": "life",
           "b2-as12": "justfriends"}

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
        words = line.split(maxsplit=3)
        lp, apg, mp = words[:3]
        if int(lp) == p:
            source = words[3] if len(words) > 3 else None
            cands.append((rmod.lt.pattern(apg), int(mp), source))
    for cfunc in rmod.cfuncs:
        if (out := cfunc(p)):
            cands.append(out + (() if len(out) > 2 else (None,)))
    if not cands:
        return []
    cands = [trip if trip[1] else (trip[0], minpop(trip[0]), trip[2]) for trip in cands]
    mp = min(trip[1] for trip in cands)
    return list(filter(lambda trip: trip[1] == mp, cands))
