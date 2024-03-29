import lifelib
sess = lifelib.load_rules("b2-as12")
lt = sess.lifetree(n_layers=1)

fixeds = """1 xs2_3 2
2 xp2_1dwd1 8
3 xp3_505 4
4 xp4_2814 4
5 xp5_342g184o 8
6 xp6_105 3
7 xp7_7daw5be 8
7 xp7_k01010kzw202 8
8 xp8_1d0201d1 10
8 xp8_44wnggzw3 10
9 xp9_a0axa0a0v 13
9 xp9_0607g6ggz6x1 13
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
22 xp22_440e0f044zx44zxe07 19
23 xp23_220fxf022zhh1sxs1hhzx1x1 27
24 xp24_vw4ay1a4wv 16
25 xp25_gg6g30ez02c122xo8zy731 22
26 xp26_1dhd1 9
27 xp27_0f0222aa2zcx603 18
28 xp28_238czxg0k07zy631c4 16
29 xp29_4k0t1t0k4z0jy1jz8b0e0e0b8zx111 36
30 xp30_y5gkk0b888zy724103y3gzgg0u0k4y94283o388zw60e021y91103zy7gmgk1a88zya6011 64
31 xp31_4k2e355l4kgz01y26 18
34 xp34_440vw434wv044zwo1y31o 22
35 xp35_s088882a20vzv0p1hgg0o0vzv01x8890vzf0454111103 65
36 xp36_883oy1o388zxv0k0k0vz11c3y13c11 38
37 xp37_oy330gzvw755xe144 19
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
56 xp56_44gb88888zx45zgg4cy131c4z01 26
58 xp58_x802141b1xg08zgx1y7g4hqzbh41y7gx1zx201xgqg4g802 32
60 xp60_o8888b8888ozwe11d11e 18
63 xp63_22o3y0kwk88kwky03o22 22
76 xp76_2r02222222220r2z0vxa0e0axvz8r08888888880r8 55
83 xp83_y311111zggybggzy4r0rz11yb11zy3ggggg 26
97 xp97_1554y2868x7o22 17
204 xp204_y38b844zgggy9cgcx888z0222yf111zya442q2 29
236 xp236_22xb1b 7
318 xp318_y3goy1448b8zy523w80kz1554zy7oy94kkgzyeo8zy62q144y131 42"""

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

p19s1 = lt.pattern("7bo$7bo$2b3o2$4o2$2b2o$5b2o$4b3o$4bo2$2bo$bo$bo")
p19s2 = [lt.pattern("3bo$b3o$b2o$4b2o2$4b4o2$3b3o$o$o")(-5,14),
         lt.pattern("8b2o$b2o$b2o$2o5bo$3bobobo$3bobobo$5bo$5bo")(13,15)]

def p19_shuttle(p):
    if p%114:
        return None
    q = p//114
    exts, r = divmod(q, 2)
    exts *= 19
    return (p19s1 + p19s2[r](exts,exts), 27, "p19 shuttle")

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
9bo$7bobo$7bobo$7bo""")(20,-6)
p34s2_3 = lt.pattern("3o9b3o2$b4o5b4o$4bob3obo$4bobobobo$4bobobobo$6bobo$6bobo$8bo")(-1,5)

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

psl1 = lt.pattern("7o2$3bo2$bo3bo2$2bobo")
psl2 = lt.pattern("o$o4bo$o$ob2o3bo$o$o4bo$o")(-12,7)
psl3 = lt.pattern("3bo$3bo$b2ob2o$2bobo2$3bo2$7o")(-5,18)
psl4 = lt.pattern("6bo$bo4bo$4o2bo$bo2bobo$4o2bo$bo4bo$6bo")(7,12)
gpsl = lt.pattern("obo$o")(1,9)

def phase_shifting_loop(p):
    y = 1
    while (p-37*y) % 26:
        y += 1
    if (x := (p-37*y) // 26) < 1:
        return None
    n_reps = [1, 12, 6, 4, 3, 12, 2, 12, 3, 4, 6, 12][p%12]
    if y*n_reps >= 10: # too many gliders to beat BG loops
        return None
    slack = p*n_reps//12 - 8
    i = 0
    match (y, n_reps):
        case (2, 1):
            minpop, gaps = 50, [1]
        case (1, 4):
            minpop, gaps = 56, []
        case (2, 2):
            minpop, gaps = 56, [0]
        case (4, 1): # x = 4 mod 6
            minpop, gaps = 56, [0, 1, 1]
        case (6, 1): # x = 3 mod 6
            minpop, gaps = 62+(x==3), [1, 1, 1, int(x>3), int(x>3)]
        case (2, 3) if p == 100:
            i, minpop, gaps = 1, 65, [0]
        case (4, 2) if p == 174:
            i, minpop, gaps = 2, 68, [0, 0, 0]
        case _:
            return None
    pat = psl1 + psl2(-i,i)[-6*i] + psl3(slack-2*i,slack)[-6*slack] + psl4(slack-i,slack-i)[-6*(i+slack)]
    gaps.append(x-sum(gaps))
    for _ in range(n_reps):
        for g in gaps:
            pat = (pat+gpsl)[37+26*g]
    return (pat, minpop, f"{n_reps}*({y},{x})-phase-shifting loop")

dl2_1 = lt.pattern("4bo$4bo$6bo$6bobo$3bo4bo$3bo6bo$2o3bo4bo$2b3ob3obo2$2obobob2o$3bobo$3bobo")
dl2_2 = lt.pattern("12bo$7b4obo$12bo$5b2o5bo$10bobo$4b3obobo$8bobo$5obo$6bo$6bo$6bo")(-5,3)
dl2_3 = lt.pattern("7b3o2$5b2o2bobo$9bobo$4b2o3bo$8bo2b3o$4o5bo$6b2obob3o$9bo$8bo2bo$8bo2bo")(-5,4)
dl2_4 = lt.pattern("""2bo2bo$2bo2bo$4bo13bo$3obob2o10bo$4bo5b4o4bobo$3o2bo14bobo$4bo3b2o2bo
3b3obobo$2bobo7bo11bo$2bobo2b2o3bobobo2b2o3bo$12bobobo7bo$4b3obobo5bo
3b2o2bo$8bobob3o2bo$6bobo7bo5b4o$6bo5b3obob2o$6bo9bo$14bo2bo$14bo2bo""")(5,-9)
dlyx = {32: (3,2), 33: (1,6), 45: (1,12), 47: (0,7), 49: (1,14), 50: (0,14),
        51: (0,8), 54: (0,2), 55: (0,9), 57: (1,18), 59: (0,10), 61: (1,20),
        62: (0,3), 64: (3,2), 65: (1,22), 66: (0,20), 67: (0,12), 69: (1,24),
        70: (0,4), 71: (0,13), 72: (1,3), 73: (2,2), 74: (1,8), 75: (0,14)}

def drifter_loop(p):
    if p not in dlyx:
        return None
    y, x = dlyx[p]
    looplen = 76 + 16*x + 92*y
    pat = dl2_1(-5,-7)
    for i in range(x):
        pat += dl2_2(5*i,5*i)
        if i == 0:
            pat ^= lt.pattern("12bo$11bobo$12bo5$2o")(-5,3)
    pat += dl2_3(5*x,5*x)
    for i in range(y):
        pat += dl2_4(24*i,0)
    pat += pat("rot180", 13+24*y+5*x, 5+5*x)
    for _ in range(looplen // p):
        pat[0,0] = 1
        pat = pat[p]
    assert pat.period == p
    return (pat, None, f"({y},{x})-drifter loop")

cfuncs = (bigglider_loop, bigglider_loop_8, p19_shuttle, p26_shuttle,
          p26_loop, p34_shuttle, p34_loop, phase_shifting_loop, drifter_loop)
