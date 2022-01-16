![Skopje's logo is a coloured Rob's p16](/logo.svg)

In May and June 2021 David Raucci (hotdogPi) on the ConwayLife forums discovered some oscillators in Conway's Life at small populations, small periods or both, which provoked me to make [a little stamp collection](https://conwaylife.com/forums/viewtopic.php?f=2&t=5338) of the smallest known non-trivial oscillators by minimum population up to p106 where I opined "the rectifier becomes more efficient than the snark for building adjustable glider loops". This turned out to be not quite right – a rectifier loop's length is of the form 8n + 2 and hence cannot have a period that is a multiple of 4 – but that gap is filled by p4 bumper and p8 bouncer/bumper loops, providing a universal upper bound of **141 cells** at **p187** and above.

This repository started out as an independent script in my glider synthesis database [Shinjuku](https://gitlab.com/parclytaxel/Shinjuku) as an automatic generator of the aforementioned glider loops and collector of other **s**mallest **k**nown **o**scillators of **p**eriods _n_ – hence the name Skopje, North Macedonia's capital. It still requires [lifelib](https://gitlab.com/apgoucher/lifelib) however.

To get the smallest known oscillator of period 109 in Conway's Life together with its minimum population:

```python
from skopje import skop
skop109, minpop109, source109 = skop(109)[0]
```

`skop()` returns a list of triples (lifelib Pattern, minimum population, description) to allow ties as in the p4, p7 and p128 cases; to get the pattern's apgcode and RLE use `skop109.apgcode` and `skop109.rle_string()` respectively. The function compares several different constructions as well as a list of fixed oscillators, LCM or otherwise, to arrive at its final result.

SKOPs in other rules can be found by passing the `rule=` argument; the supplied string gets run through lifelib's `sanirule()` function before being mapped to a filename. The file itself should contain three objects:

* `lt`, the lifetree under which computations are performed.
* `fixeds`, a multiline string where each line gives the period of a fixed oscillator, its apgcode and its minimum population, all separated by spaces.
* `cfuncs`, a sequence of functions each accepting a period and returning `None` if its corresponding construction is not applicable to that period or (Pattern, minimum population) otherwise. The latter element can itself be `None` to indicate that the period is in a range where the population does not follow a defined formula.
