import lifelib
sess = lifelib.load_rules("b2-as12")
lt = sess.lifetree(n_layers=1)

fixeds = """1 xs2_3 2
2 xp2_1dwd1 8
3 xp3_505 4
4 xp4_2814 4
5 xp5_1h1g46o 10
6 xp6_105 3
7 xp7_k01010kzw202 8
8 xp8_1d0201d1 10
9 xp9_a0axa0a0v 13
10 xp10_011k44z444gi 12
11 xp11_jwa0bz1 9
12 xp12_5xk 4
13 xp13_c31y113czy0707 13
14 xp14_10d 4
15 xp15_0o0704kgz454gkg 17
16 xp16_c201gczw1 8
17 xp17_oy5414w70ozw7w141 16
18 xp18_8c0704x88zw1d028 15
19 xp19_xlkl44z3 12
20 xp20_03z1t1g7zx703 15
21 xp21_22w98j44 10
22 xp22_u0gwa0vzvwexf 24
23 xp23_220fxf022zhh1sxs1hhzx1x1 27
24 xp24_vw4ay1a4wv 16
25 xp25_8g6g30ez03c122xo8zy731 23
26 xp26_1dhd1 9
27 xp27_0f0222aa2zcx603 18
28 xp28_238czxg0k07zy631c4 16
29 xp29_4k0t1t0k4z0jy1jz8b0e0e0b8zx111 36
30 xp30_y5gkk0b888zy724103y3gzgg0u0k4y94283o388zw60e021y91103zy7gmgk1a88zya6011 64
31 xp31_4k2e355l4kgz01y26 18
34 xp34_440vw434wv044zwo1y31o 22
35 xp35_s088882a20vzv0p1hgg0o0vzv01x8890vzf0454111103 65
36 xp36_883oy1o388zxv0k0k0vz11c3y13c11 38
37 xp37_11d1d11wszwgzw3w88b8b88 26
38 xp38_gg0o1t1d1hhzw602 21
39 xp39_880mg788gg887gm088zw5x55w55x5z03ya3 38
40 xp40_v0804080vzv0325230v 29
41 xp41_vxk88xez3y345011 18
42 xp42_4o340ax886zxc 14
43 xp43_woy170e0ozo0f0fxq0q0fzf0p0hx30fzw103 42
43 xp43_238cy1gy0gy1c832zy4glk11klgzy1450q2y02q054 42
44 xp44_cy0c832z0cgczz3y031c4 18
46 xp46_y1qx8wvzowg4wo1z7y22 20
48 xp48_4o3o2z1060c07 16
53 xp53_y72q28f82q2zy2gw2245y15422wgz0e0k4416yb6144k0ez1t1b880oybo088b1t1zy23wgg88y188ggw3zy7gng4s4gngzyb1 100
54 xp54_y6gg888888a20vzy2s08aaa0e0s0l5l0r4118822q2gzy1o1060c0k5l7gf098jkk1t0o0b8b03sz2q2i2o0o0aa21c3w3x442k55ll1t0s0f0ozxv01glk5t5t1a99gg0m80e1c2i2xo22222zx160e0uwgl411u0c0f0v5l1ghgj0szy32222w441u05llghgjgaa2w1zyc7022 276
56 xp56_gg4881lh88hl1884ggzx307y2703 34
58 xp58_x802141b1xg08zgx1y7g4hqzbh41y7gx1zx201xgqg4g802 32
60 xp60_o8888b8888ozwe11d11e 18
63 xp63_22o3y0kwk88kwky03o22 22
76 xp76_2r02222222220r2z0vxa0e0axvz8r08888888880r8 55
83 xp83_y311111zggybggzy4r0rz11yb11zy3ggggg 26
97 xp97_22o7x868y7868x7o22 22
236 xp236_22xb1b 7"""

bgl1 = lt.pattern("bo$bo$3b6o$3o")
bgl2 = lt.pattern("2bo$2bo$2bo$2bo$2bo$2bo$3bo$2obo$3bo")(-2,7)
bgl3 = lt.pattern("6b3o$6o$7bo$7bo")(5,14)
bgl4 = lt.pattern("o$ob2o$o$bo$bo$bo$bo$bo$bo")(12,2)
gbgl = lt.pattern("obo$o$2bo$2bo")(5,5)

def bigglider_loop(p):
    if not p%3 or p < 76:
        return None
    if p%12 == 8 and p >= 212:
        n_gliders, i, mpop = (1, 0, 46)
    elif p%3 == 2:
        n_gliders, i, mpop = (4, p//6-8, 52 if p%6 == 5 else 56)
    elif p%6 == 4 and p >= 130:
        n_gliders, i, mpop = (2, 2, 48)
    elif p%12 == 4:
        n_gliders, i, mpop = (5, p//6-8, 70)
    elif p%3 == 1:
        n_gliders, i, mpop = (8, p//6-8, 80 if p%6 == 1 else 82)
    slack = (p*n_gliders - 212) // 12
    pat = bgl1 + bgl2(-i,i) + bgl3(slack-2*i,slack) + bgl4(slack-i,slack-i)
    for _ in range(n_gliders):
        pat = (pat+gbgl)[p]
    return (pat, mpop, f"{n_gliders}BG loop")

bglf8_0 = lt.pattern("2bo$2bo$2bo$2bo$2bo$2bo$3bo$2obo$3bo$2bo$2bo$2bo$2bo$2bo$2bo")(-3,-7)
bglf8_1 = lt.pattern("16bo$16bo$16bo$16bo$16bo$16bo$15bo$15bob2o$15bo2$3o$3b6o$bo$bo")(-1,1)
bglf8_2 = lt.pattern("bo$bo$3b6o$3o2$15bo$15bob2o$15bo$16bo$16bo$16bo$16bo$16bo$16bo")(-1,-14)
gbglf8 = lt.pattern("2obo2$2b2o")(9,2)

def bigglider_loop_8(p):
    if p%3 or p < 81:
        return None
    if p%12 == 0 and p >= 420:
        n_gliders, i, mpop = (1, 0, 63)
    elif p%6 == 0 and p >= 252:
        n_gliders, i, mpop = (2, 0, 65)
    elif p >= 138:
        n_gliders, i, mpop = (4, p//6-21, 77 if p%6 else 75)
    else: # TODO other numbers of gliders (3, 5, 6, 7)
        n_gliders, i, mpop = (8, p//3-21, None)
    slack = (p*n_gliders - 420) // 12
    pat = bglf8_0 + bglf8_1(i,i) + bglf8_2(slack-i,i-slack)
    if p == 420:
        pat[15,0] = 1
        mpop += 1
    for _ in range(n_gliders):
        pat = (pat+gbglf8(i,i))[p]
    return (pat, mpop, f"{n_gliders}BG figure-8 loop")

p26s1 = lt.pattern("5o4$bobo$2bo$2bo4$bo$o$o")
p26s2_0 = lt.pattern("2bo$2bo$bobo4$5o")(-6,13)
p26s2_3 = lt.pattern("4bo$b2obo$o3bo$b2obo$4bo")(11,11)

def p26_shuttle(p):
    if p%78 or p < 78:
        return None
    q = p//26
    exts, r = divmod(q, 6)
    exts *= 13
    if r == 0:
        return (p26s1 + p26s2_0(exts,exts), 21, "p26 shuttle")
    elif r == 3:
        return (p26s1 + p26s2_3(exts,exts), 22, "p26 shuttle")

p26l1 = lt.pattern("5o2$bobo$bobo$2bo")
p26l2 = lt.pattern("o$o2b3o$o2bo$o2b3o$o")(-6,10)
p26l3 = lt.pattern("2bo$bobo$bobo2$5o")(4,16)
p26l4 = lt.pattern("5bo$3o2bo$2bo2bo$3o2bo$5bo")(9,6)
gp26l = lt.pattern("o$b2o")(3,8)

def p26_loop(p):
    if p%26 or not p%78 or p < 52:
        return None
    r = p//26%6
    if r == 4:
        n_gliders, i, mpop = (1, 0, 39)
    elif r == 2 or r == 5:
        n_gliders = 2
        i, mpop = (2, 46) if p == 52 else (4, 42)
    elif r == 1:
        n_gliders, i, mpop = (4, 4, 48)
    slack = (p*n_gliders - 44) // 12
    pat = p26l1 + p26l2(-i,i)[-6*i] + p26l3(slack-2*i,slack) + p26l4(slack-i,slack-i)[-6*i]
    for _ in range(n_gliders):
        pat = (pat+gp26l)[p]
    return (pat, mpop, f"{n_gliders}G p26 loop")

p34s1 = lt.pattern("""8bo$6bobo$6bobo$6bo$3b2obo11b2o$11b3o3bo$7o5b2o$10bobob2o$b6o5b2o$11b
3o$3b2obo$6bo$6bobo$6bobo$8bo""")
p34s2_0 = lt.pattern("""7bo$7bobo$7bobo$9bo$9bob2o$2b3o$2b2o5b6o$2obobo$2b2o5b7o$2b3o$9bob2o$
9bo$7bobo$7bobo$7bo""")(37,11)
p34s2_3 = lt.pattern("3o9b3o2$b4o5b4o$4bob3obo$4bobobobo$4bobobobo$6bobo$6bobo$8bo")(16,22)

def p34_shuttle(p):
    if p%102:
        return None
    q = p//34
    exts, r = divmod(q, 6)
    exts *= 17
    if r == 0:
        return (p34s1 + p34s2_0(exts,exts), 49, "p34 shuttle")
    elif r == 3:
        return (p34s1 + p34s2_3(exts,exts), 65, "p34 shuttle")

p34l1 = lt.pattern("""20bo$20bobo$20bobo$18bobobobo$18bobobobo$20bobo$15b4obobob4o2$14b3o9b
3o2$21bo$19bo3bo$19b5o$19b2ob2o$21bo$21bo$8bo$6bobo$6bobo$6bo$3b2obo$
11b3o$b6o5b2o$10bobob2o$7o5b2o$11b3o$3b2obo$6bo$6bobo$6bobo$8bo""")
p34l2 = lt.pattern("""20bo$20bobo$20bobo$22bo$22bob2o$15b3o$15b2o5b7o$13b2obobo$15b2o5b6o$
15b3o$22bob2o$22bo$20bobo$20bobo$20bo$7bo$7bo$5b2ob2o$5b5o$5bo3bo$7bo
2$3o9b3o2$b4obobob4o$6bobo$4bobobobo$4bobobobo$6bobo$6bobo$8bo""")(16,14)
gp34l = lt.pattern("obo$o")(22,17)

def p34_loop(p):
    if p%34 or not p%102:
        return None
    r = p//34%6
    if r == 4:
        n_gliders, mpop = (1, 95+(p==136))
    elif r == 2 or r == 5:
        n_gliders, mpop = (2, 98+2*(p==68))
    elif r == 1:
        n_gliders, mpop = (4, 104+4*(p==34))
    slack = (p*n_gliders - 136) // 12
    pat = p34l1 + p34l2(slack,slack)
    for _ in range(n_gliders):
        pat = (pat+gp34l)[p]
    return (pat, mpop, f"{n_gliders}G p34 loop")

psl1 = lt.pattern("12b7o2$15bo2$13bo3bo2$14bobo$o$o4bo$o$ob2o3bo$o$o4bo$o")
psl2 = lt.pattern("18bo$13bo4bo$12b4o2bo$13bo2bobo$12b4o2bo$13bo4bo$3bo14bo$3bo$b2ob2o$2bobo2$3bo2$7o")(7,12)
gpsl = lt.pattern("obo$o")(13,9)

def phase_shifting_loop(p):
    # Determine if the period can be represented by the loop;
    # p must be of the form 26x + 37y with x, y >= 1
    # Furthermore we take y (the number of glider-containing segments)
    # to be as small as possible
    # All periods at least 26*37+1 = 963 can be represented this way
    # TODO handle different loop shapes and different glider positions in a repetition
    y = 1
    while (p-37*y) % 26:
        y += 1
    if (x := (p-37*y) // 26) < 1:
        return None
    n_reps = [1, 12, 6, 4, 3, 12, 2, 12, 3, 4, 6, 12][p%12]
    slack = p*n_reps//12 - 8
    pat = psl1 + psl2(slack,slack)[-6*slack]
    for _ in range(n_reps):
        for _ in range(y):
            pat = (pat+gpsl)[37]
        pat = pat[26*x]
    return (pat, None, f"({y},{x})-phase-shifting loop")

dl1 = lt.pattern("""20bo2bo$13b6obo2bo$11b2o9bo$18b3obob3o3bo$10b3obo7bo4b2obo2bo$7bo6bobo
b3o2bo6bo2bo$7bob4obobo5bo3b2o2bobo2b2o$7bo10bobobo7bobobo$7bo5b2o3bob
obo2b2o3bobobo$9bo8bo3bo7bobobo$9bobob3o2bo4b2obobo5bo$6bo4bo6bob2o4bo
bob3o2bo$bo4bo6bobobo3bo2bobo7bo$bob2o3bo4bobo2bo5bo5b3obo$bo3b3ob4o2b
o2bo5bo9bo$bo12bo10b6obo2bo$o2b2obobob3obo7b2o8bo2bo$obo3bobo14bo2bobo
b2o$2bobobobob7o9bobo4b4o$4bo21bo4b2o$b2obo3b2o5bo$4bo8bobo$3obo2b3obo
bo2bo$4bo6bo4bo$5b3o8bo$2b2o$3bo""")(-34,-11)
dl2 = lt.pattern("""38bo$38bo4bo3b2o$39b4ob3o$36b2o$37bo2b2obobob2o$20bo2bo19bobo$13b6obo
2bo10b2ob5obobobo$11b2o9bo13bo10bo$18b3obob3o3bo11b2o3bo$10b3obo7bo4b
2obo3b3obo8bo$7bo6bobob3o2bo6bob2o4bobob3o2bo$7bob4obobo5bo3b2o2bo4b2o
bobo6bo$7bo10bobobo7bobobo7bobobo$7bo5b2o3bobobo2b2o3bobobo2b2o3bobobo
$9bo8bo3bo7bobobo7bobo$9bobob3o2bo4b2obobo5bo3b2o2bo$6bo4bo6bob2o4bobo
b3o2bo$bo4bo6bobobo3bo2bobo7bo5b4o$bob2o3bo4bobo2bo5bo5b3obob2o$bo3b3o
b4o2bo2bo5bo9bo$bo12bo10b6obo2bo$o2b2obobob3obo7b2o8bo2bo$obo3bobo14bo
2bobob2o$2bobobobob7o9bobo4b4o$4bo21bo4b2o$b2obo3b2o5bo$4bo8bobo$3obo
2b3obobo2bo$4bo6bo4bo$5b3o8bo$2b2o$3bo""")(-43,-2)
dl3 = lt.pattern("""6bo11bo$6bo4bo3b2obo$7b4ob3o3bo$4b2o12bo$6b4obobob2o2bo$11bobo3bobo$3b
7obobobobo$15bo$4bo5b2o3bob2o$4bobo8bo$3bo2bobob3o2bob3o$3bo4bo6bo$3bo
6bob3o$2o3bo4bo5b2o$2b3ob4o6bo$11b2o$2obobob2o2bo$3bobo$bobobob5ob2o$b
o10bo$bo3b2o11bo3b3o$bo8bob3o3bob2o$bo2b3obobo4b2obo$bo6bobob2o4bo2b2o
$2bobobo7bobobo$2bobobo3b2o2bobobo3b2o$4bobo7bobobo$6bo2b2o3bo5bobo$
13bo2b3obobo$5b4o5bo7bobo$11b2obob3o5bo$14bo9bo$13bo2bob6o$13bo2bo8b2o
$17b2obobo2bo$12b4o4bobo$16b2o4bo""")(-11,-2)
dl4 = lt.pattern("""4b2o4bo$4o4bobo$5b2obobo2bo$bo2bo8b2o$bo2bob6o$2bo9bo$2bob3o5bo5bo3b3o
$2bo7bobo2bo2bob2o$bo2b3obobo4bo2bo$2bo5bobob2o2bobo2b2o$2bobobo7bobob
o$2bobobo3b2o2bobobo3b2o$2bobobo7bobobo$2o2bobo2b2o3bo5bobo$3bo2bo6bo
2b3obobo$3bo2bob2o4bo7bobo$6bo3b3obob3o5bo$14bo9bo$13bo2bob6o$13bo2bo
8b2o$17b2obobo2bo$12b4o4bobo$16b2o4bo""")(-2,-8)

def drifter_loop(p):
    """Construct a drifter loop of period p using Dean Hickerson's
    universal 23-gen and 27-gen components. Requires the PuLP solver
    for finding the optimal loop parameters through integer linear programming."""
    if p < 13 or p >= 76:
        return None
    # Minimise 71x + 36y subject to x, y >= 1 and q | 50x + 23y
    # where q is a quarter of the "effective period" (p times how many drifters
    # are needed to get a multiple of 4). The actual x and y are then these
    # variables decremented
    from pulp import LpProblem, LpVariable, PULP_CBC_CMD
    q = p if p%2 else p//2 if p%4 else p//4
    lp = LpProblem()
    a = LpVariable("a", cat="Integer")
    b = LpVariable("b", cat="Integer")
    lp += (6*q*b - 23*a >= 1, "x")
    lp += (50*a - 13*q*b >= 1, "y")
    lp += (71*(6*q*b - 23*a) + 36*(50*a - 13*q*b), "population")
    lp.solve(PULP_CBC_CMD(msg=False))
    sols = {v.name: int(v.varValue) for v in lp.variables()}
    a, b = sols["a"], sols["b"]
    x = 6*q*b - 23*a - 1
    y = 50*a - 13*q*b - 1
    looplen = 200*(x+1) + 92*(y+1)

    pat = dl1(0,0)
    cx, cy = -20, 15
    for _ in range(x):
        pat += dl2(cx,cy)
        cx -= 29
        cy += 29
    pat += dl3(cx,cy)
    cx += 15
    cy += 20
    for _ in range(y):
        pat += dl4(cx,cy)
        cx += 24
    pat += pat("rot180", cx, cy)
    for _ in range(looplen // p):
        pat[0,0] = 1
        pat = pat[p]
    return (pat, None, f"({x+1},{y+1})-drifter loop")

cfuncs = (bigglider_loop, bigglider_loop_8, p26_shuttle, p26_loop, p34_shuttle, p34_loop,
          phase_shifting_loop, drifter_loop)
