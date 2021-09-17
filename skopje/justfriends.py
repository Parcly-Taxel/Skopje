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
26 xp26_1dhd1 9
27 xp27_88888q22y1u07z0h1uy3c89aa8z0301y1111 36
28 xp28_xggx440b8zwow10cz2207 18
29 xp29_4k0t1t0k4z0jy1jz8b0e0e0b8zx111 36
34 xp34_440vw434wv044zwo1y31o 22
35 xp35_s088882a20vzv0p1hgg0o0vzv01x8890vzf0454111103 65
36 xp36_883oy1o388zxv0k0k0vz11c3y13c11 38
37 xp37_11d1d11wszwgzw3w88b8b88 26
40 xp40_v0804080vzv0325230v 29
41 xp41_vxk88xez3y345011 18
42 xp42_4o340ax886zxc 14
43 xp43_woy170e0ozo0f0fxq0q0fzf0p0hx30fzw103 42
44 xp44_8b8444448b8zy0cgczz1d1222221d1 31
46 xp46_y1qx8wvzowg4wo1z7y22 20
53 xp53_y72q28f82q2zy2gw2245y15422wgz0e0k4416yb6144k0ez1t1b880oybo088b1t1zy23wgg88y188ggw3zy7gng4s4gngzyb1 100
56 xp56_gg4881lh88hl1884ggzx307y2703 34
60 xp60_o8888b8888ozwe11d11e 18
63 xp63_22o3y0kwk88kwky03o22 22
76 xp76_2r02222222220r2z0vxa0e0axvz8r08888888880r8 55
83 xp83_y311111zggybggzy4r0rz11yb11zy3ggggg 26
97 xp97_22o7x868y7868x7o22 22
236 xp236_22xb1b 7"""

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
        return (p26s1 + p26s2_0(exts,exts), 21)
    elif r == 3:
        return (p26s1 + p26s2_3(exts,exts), 22)

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
    return (pat, mpop)

cfuncs = (p26_shuttle, p26_loop)
