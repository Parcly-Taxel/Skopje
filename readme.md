![Skopje's logo is a coloured Rich's p16](/logo.svg)

In May and June 2021 David Raucci (hotdogPi) on the ConwayLife forums discovered some oscillators in Conway's Life at small populations, small periods or both, which provoked me to make [a little stamp collection](https://conwaylife.com/forums/viewtopic.php?f=2&t=5338) of the smallest known non-trivial oscillators by minimum population up to p106 where I opined "the rectifier becomes more efficient than the snark for building adjustable glider loops". This turned out to be not quite right – a rectifier loop's length is of the form 8n + 2 and hence cannot have a period that is a multiple of 4 – but that gap is filled by p4 bumper and p8 bouncer/bumper loops, providing a universal upper bound of **141 cells** at **p187** and above.

This repository started out as an independent script in my glider synthesis database [Shinjuku](https://gitlab.com/parclytaxel/Shinjuku) as an automatic generator of the aforementioned glider loops and collector of other **s**mallest **k**nown **o**scillators of **p**eriods _n_ – hence the name Skopje, North Macedonia's capital. It still requires [lifelib](https://gitlab.com/apgoucher/lifelib) however.

To get the smallest known oscillator of period 109 together with its minimum population, a rectifier loop:

```python
from skopje import skop
skop109, minpop109 = skop(109)[0]
```

`skop()` returns a _list_ of pairs (lifelib Pattern, minimum population) to allow ties as in the p4 and p7 cases; to get the pattern's apgcode and RLE use `skop109.apgcode` and `skop109.rle_string()` respectively. The function compares several different constructions as well as elementary (non-loop) and LCM oscillators to arrive at its final result.

Each function producing oscillators of a certain type for an infinite number of periods should accept the desired period as its argument and return `None` if the construction is not applicable to that period or (Pattern, minimum population) otherwise. The latter element can itself be `None` to indicate that the period is in a range where the population cannot easily be calculated.
