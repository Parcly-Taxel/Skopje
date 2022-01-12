import lifelib
sess = lifelib.load_rules("b3s23")
lt = sess.lifetree(n_layers=1)

fixeds = """1 xs4_33 4
1 xs4_252 4
2 xp2_7 3
3 xp3_4hh186z07 12
4 xp4_37bkic 12
4 xp4_ssj3744zw3 12
5 xp5_y2g0k413zwo0a02z32 15
6 xp6_ccb7w66z066 16
7 xp7_0g88b5oz1255kk3033zy011 28
7 xp7_o8bbc0sz017871x31e8 28
7 xp7_o8y2gbdz0dl31w11156z011 28
7 xp7_5b8b94gszw652y06a8o 28
8 xp8_gk2gb3z11 12
9 xp9_0c93wmk46z69bo7421 29
10 xp10_c846l3wszy03wca6213 24
11 xp11_y0dbzggci5ld3xog8oz0343 33
12 xp12_032acy0oge2z0g8ow77ggz23y21226 33
13 xp13_gy1gr3zd5a64210g8c4066zy2kr6og 34
14 xp14_j9d0d9j 16
15 xp15_4r4z4r4 12
16 xp16_0c2w3vz33032988 21
17 xp17_32acy1ca23zy27rszwo8a6y16a8o 36
18 xp18_66625ak8zy177xcc0cczy1g8mwiozx91gp 43
18 xp18_wc93xs112ogggzbdhe96kk801zw1213 43
20 xp20_35426ow37bkicz65123 30
21 xp21_5b8b94gszw6520gw6a8ozx332f7zy2121 40
22 xp22_178cwggg2y2oo4kozy235433y28111w62sg 36
23 xp23_y1ggy3o8bdzc82u074wo84s8x31560u28czx11y0hi21y411zy5ddx696zgg0s4y1owsi1isx4s0ggz10230f9y3ogjn45303201zyc65 122
24 xp24_xsssx4hh186z777y37 24
25 xp25_w696o8b9cxc9b8o696zbt065x31x13x56z0123x8c8x8c8zxggkcy2oox31e8zx1 83
26 xp26_0c4o796kcimkk8goz4aajkm0fomi87kggzca245l4870122c543zy111 87
27 xp27_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910oo 56
28 xp28_033y133zo4maxam4oy1ggz1ppy1pp1xsta43 46
29 xp29_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11zzy8252y1252 54
30 xp30_w33z8kqrqk8zzzw33 20
31 xp31_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066 48
32 xp32_wosq596zy3oy0c871zy2525z66zgggeeez333 45
33 xp33_8ehe8oy1o8a6zw12ll64x88c04c6ezy056y313 46
35 xp35_y4ok46y3253zooxgcgy47r4xcczxgw33y0ggkczw321y31 44
36 xp36_32aczy08c8y0131zya354c 22
37 xp37_y2gy033y733y0gzy02543y130aic0cia03y13452z66x88yj88x66zy23kl2yd2lk3zggx8b021yd120b8xggz11xggy484o0o48y4ggx11zy01243y13011x1103y13421zy733y733 124
39 xp39_xqh2z33173xccz4sk0emicy2oozy469dezy4327 46
40 xp40_33zxs48g69gvzx3021zy833 26
42 xp42_033y133zo4maxam4oz1ppy1pp1xgfnzyb1252333 50
44 xp44_0oql96xmqzgh1gxeqaa4oz1011y217871 45
45 xp45_vtvy2j9e0o4cz757y1ojhrhla23zy666 48
46 xp46_033y133zzzckgsxsgkczz0cc 28
47 xp47_w32acyeca23zy37y2ccy27z252xeaey8eaex252zg8gxsksy8sksxg8gz01y1oy2ccy2oy11zwggkc01ya10ckggzw1yk1 84
48 xp48_s22t3wg8gzo55txdl8z12256zy566w7bcczya66 52
49 xp49_y6gbd0uik8y5ggozy4622dh5nqlxgg8x32y6ggzy5311x33x246y71784cj4ic84czx178cyn46xe6e853zy5o84cygc846z0g84sosxo8ync4ozc95ci8ic84oy8o8gxggy1gy011zy232w11y2ggx422xbnq82dhhozyc6221y44biv1dl2zyt11 206
50 xp50_3p6w6p3z0102201xidiidizws01110sw1w1zy0222zx4r4zzzy04r4x8k88k8z0s0220sx252252z643w346 92
51 xp51_g08o0u15gis89f0s48cz11wdbaik68jd0ddy1ca23zy232011y1sr7zy6o8a6y16a8o 90
52 xp52_4s0gy3ca23zw11w4ed3zy08oy362sgzw311 35
54 xp54_32acy5ca23zy1ooxoozx4ossxsso4zzzc453y5354c 48
55 xp55_y0dby06a8gzggci5ld3xogg150cgz0343y523y0346 49
56 xp56_66625dw66zyb66zzy0oow8s26zy61ooo8kkwoozyc1 45
57 xp57_y8o08868y3ca23zy6cb2807x6msy44s0ggzggy0c453yi1044pq0kgz0346ysh3040ezy3r96yk69dzw7gi0soys62sgzy020592ig8gy5ggy6ca23zy832y4366xe01kd3zybc453y3161101 152
58 xp58_wj9ary9ra9jzwdl4cy9c4ldz311yf113z32qkgow262x262wogkq23zw6a8cy9c8a6zw3213y93123 104
60 xp60_vtvy037bkicz757 24
62 xp62_ccy069c536635c96y0cczz66y0ci6koccok6icy066zzy4ojd11djo 66
63 xp63_32acxca23wgg8g0g8ggzy04r4y07fmoc707comf7zy04r4y2ccy1cczo8a6x6a8o 78
64 xp64_y1j3zy031d8ey633zggy6s4c0gz11y8hj1zya11 34
65 xp65_3pmwmp3zxh1gx21h2zx3c7a5301gk2w96zy5admlk 52
66 xp66_y2ca23zws21q4zx11zxgc22szw8o121z311y0681hh4zy77 48
68 xp68_w32acy1ca23zy2sr7zo8a6y1mm0mp2c82u08ozy51qaic0d5521 72
69 xp69_yco08868y3ca23zyacb2807x6msy6ggzy6c453yj346co8oggz8oyz04t0vqgz0123ywog488w1zwgw22413ywo8gzw1bv0n4yz032zy0113236c4oyjok46zy811y67dcxs028q6zydo8a6y32c2203 152
70 xp70_033y133y1o62453zo4maxam4oy132156z1ppy1pp1 52
72 xp72_3bg2kgzy011y7ok46zy268ga4w8k24ozxo8a6 36
74 xp74_y532acy5ca23zggyrggz0346y5636404636y5643zz0o4cy5coc404cocy5c4oz11yr11zy5o8a6y56a8o 84
76 xp76_c4o796zuvvy4sgszc97o4ozx11zyf697o4czy7e2ey4vvuzyfo4o79czyg11 82
77 xp77_wo8gwog4cgcip688gzxgbao8y2nk5o7ioz4s3s57y1642sj43zw1 77
78 xp78_y45rc31zwmkac48g012640cczw1wgw1rozmkgino3s4z1w6221 61
80 xp80_35426ox22i8o0ooz65123y1vow86 39
81 xp81_yh32acy386880ozyosm6x7082bczy8o8ym354czy080ki89121zws19073yzy1c871zy3ricywcimz0o4cyzy1ho040ez11yzxg044jb051zy8c88gym47011zya11ckg40oxoqezyd16045o4y3ckggzyu1 152
84 xp84_yf8ka52666zy5c66mkg8y077zzxgy1215dcc6z4ql21333z033 52
85 xp85_w32acy1ca23zy2sr7zo8a6y1mm0mp3c48cggzy5122m031fhd221zy811 74
87 xp87_ya32aczyfg8gw33y466zxg8gy81221zggw1oogyesscz11y2deeyd1266x33zycggy9252z0ooy4ggw3421zy711y2ckggzyi1 84
88 xp88_3bg2kgzy011y1o4oz3213xgonl9611zy5qm 45
90 xp90_w33z8kqrqk8zy6cczy43llhhla8ozw33y1pie0346 56
91 xp91_gy1gr3zd5a64210g8c4066wckzy2kr6ogy0f5lc3c4ozybogno311zyb32qm 78
92 xp92_yi33y133zzzyhckgsxsgkczz33y7c20197zccy734089e 50
92 xp92_66ybb9ey366zooybk4sya3920skzyd11y9494721023 50
93 xp93_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy44hh186zy57 60
94 xp94_x696o8b9czy065x33xc871xggzooyd643zwgg04ahhha4y5c871z4701yfoozw8e13xggzy34701xmmggo5jzya146w343 110
96 xp96_0178cy766zy44koy6m640ooe4a4z0gs26x11xoy1oo022440ezo8go 59
98 xp98_y232acy0o4c88gy7mqzy735430311yi88ge2z0og8oyl754y2qkigzy666yn2ege3zzwgs2sgynoozw12iamy288oyl6426zgs244y511y9g0g88gzy9mqy7255d870110ckggzyz1 146
99 xp99_8oy3nl6z0123ws21913z8e13x12mmjy3mqzy53210gxeqaa4ozy66511y217871 82
100 xp100_178cyao8gy0ccy0g8oyac871zye1m31y5322z0g8oyae972xooy079dyao8gz23yzy532 70
102 xp102_y6oo033wgwgggy1gggwgw330oozya4e9130111y11110319e4zya77yf77zyaooyfoozya9t40gy9g04t9zy6660gg01310333y133301310gg066zy911w82095wgggy511zyed0ho82321zzgg066yh660ggz11w8si360333y1333063is8w11zy0eeyfeezy0ggyfggzy0jr8yd8rjzccx12630666y166603621xcczx33yh33 249
104 xp104_gk2gb3y013cr5z11y0cc046210g84cakmzy8or1y11 46
105 xp105_0oggxooy1vtvzc88m5o0ccy1757zw1qm0f952 49
108 xp108_wc4o0oy6g033zougdb158cy1a9871zy0ooyf789q8zy42bi2syf33zyfgs2iazydoo01 78
110 xp110_c4oy1178cwggg2y2oo4kozx160kgy235433y28111w62sgzy412ac 51
112 xp112_om999e0e999mozx8kc0ck8zzw8if505fi8 50
113 xp113_y98oyn33y166z8oy732ys33y0ccz01219g8y2gkszwcq2qbyzy18e1eozx121ywsk4y2b591zxooyzy5221e8zy3gg33ysdbzy311y133 106
116 xp116_y4o8bp688gz0gy6330pq2cggz121x225y49f023z8k8x44ay296zy8mmg6p2s82u08ozy81qaic3c4521 102
117 xp117_y1o44mhar0rahm44ozwg8p7870167876107871zq6hcbagy1szg9gf99gfy26a8oz56o3t5zx1 117
120 xp120_4r4y13bg2kgz4r4y511 24
124 xp124_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy337bkic 60
126 xp126_0ccy1ccx32acxca23zcmkgxgkmcy24r4zy0202y64r4z033y133xo8a6x6a8o 74
128 xp128_y3ca73oswcczyqg88gzy1ggyh6bbcxca4z8ko010onmcy04eewuscy26dt30g0352z4a6x6qqcyh11zy01221zyh66w73osa6 108
129 xp129_yro08868y3ca23zypcb2807x6mszylc453zzyzynggzyzyo346co8oggz8oyzyr4t0vqgz0123yzynog488w1zwgw22413yzyno8gzw1bv0n4yzyr32zy0113236c4ozy811zzyzy8ok46zyz7dcxs028q6zyso8a6y32c2203 152
130 xp130_og8o0u1eozy0mlgrzx1qa2my2meiz62460v0t60gg037fa60ggzy21x11y236fe5267zyc33 89
132 xp132_252w253zy0gxggg0ooozy13w3488a61oml1hiswcgzw695qsoy3111zyica4w4a4 72
135 xp135_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910ooy2uquzyjfbf 68
138 xp138_w8gw259r84z79431y1go4iszx42rik8w12 36
140 xp140_033y133zo4maxam4oy1gy1gs26z1ppy1pp1y0121ggcaaq552zy8ok46o7o7421zyd1 82
141 xp141_y64a4y14a4w178cx8e1e8gzy2sy0cscxcscy0sx33159d11z8e13yj31e8z8oy133y933y1o8z0123wsy0osoxosoy0sw321zy6g8gy1g8gzy71y31 114
144 xp144_33y18kk8yb33zy8equzy9757wggzccyb1221y1cc 42
152 xp152_ykokct04zc4o796yc10511zuvvy4sgszc97o4ozx11zyf697o4czy7e2ey4vvuzyfo4o79czyg11 94
156 xp156_yg33zy1ogg178cy2iey6c871ggozy323yk32zy2ogg8z33yq844cy033zzy1c453g8oy6o4y2o8g354czy423y811y432zyg33 92
160 xp160_0db0gy0ooy3gokaicz651230sw224oy1111wgy0oge2zggy0s03wgfy5a5az1qa17y0ddy1ccz023ycssszyc777 101
165 xp165_y0dbzggci5ld3xog8oz0343zy275777757 45
168 xp168_y68e13zy0o4ogw315b8oz0gx11z121y6252y2g0oozc88gy04eicy4cd042zw32qbzw321 72
170 xp170_y6438g0ia4zx66w66xac4zxggo4c4oggyh66x66zca16888188861acya358mhh181hhm853zy066x66yj12321zyv66w66zym252x66 119
177 xp177_y3343x6bacy6cab6x343zkk8yy8kkzgo8gywg8ogz0123yw321zzgo4syws4ogzgh1yy1hgz221yy122zy3c2cx6d53y635d6xc2c 104
184 xp184_33y7cccd72ycssszccy7333be4y4ccy5777 40
186 xp186_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy0ccb7w66zy166 64
188 xp188_x696o8b9czy065x33xc871wbdzoozwgg04ahhha4y5c871z4701yfoozxggy0ggzx56w4701xmmggo5jzya146w343 108
196 xp196_yfccy28e1e88gzyeks8y2330311zyqoozwggzw11y6ggzg88c0ccy2132z0117871y233 66
200 xp200_178cyao8gy0ccy0g8oyac871zye1m31y5322z0g8oyae972xooy079dyao8gz23yiggyk32zygoq1851 82
226 xp226_y98oyn33y166z8oy732ys33y0ccz01219g8y2gkszwcq2qbyzy18e1eozx121yv8km8y27d11zxooyzy631e8zy3gg33ysdbzy311y133 107
228 xp228_yf697o4czy7sgsy4vvuzyfo4o79czyg11zc4o796zuvvy4e2ezc97o4ozx11y9ccwemoozyjcc 98
230 xp230_033y133zzzckgsxsgkczzy4cczxggzojdwdjo 46
232 xp232_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11z0gggeeez0333y4252y1252 66
240 xp240_4r4y11h94c0ccz4r4y2fcw43 33
246 xp246_ya32acydg8k8ooozyu1utzzzybcirrd6y4cc4zy1ggy61zggwg9g89z14w61ye354c 68
250 xp250_y1ooy2o4a9jwggzy1ccy0elh4wrwhhz33x6a2y134aipw11z252zzzzykggy94a4zygoowp452sgy6cczygoowtw2oa7y0jjzykc9521y211 119
256 xp256_yr33y166z0ggy033y4178cyb33y0ccz011w66z66yyg88czy4699voyn11zy38ox61zy1311yz66zyzx66woozy133y0ccyb31e8y4cczy566y1cc 104
276 xp276_02hqzw37133zy9ei204oy766zy9sig086y7oozz6517x7156zzz0ooy1oo 62
288 xp288_ggc2sgy3osq596z694r2a3sy6oy0c871zci4r8ao7y5525z116871y166zy7gggeeezy7333 95
304 xp304_yf697o4czy7sgsy4vvuzyfo4o79czyg11zc4o796zuvvy4e2ezc97o4ozx11y84a404u6kezyg4sh93 103
312 xp312_yg33zy1g8gy6ieyag8gzy1121ym121zy2ogg8z33yq844cy033zzy1696yao4y6696zyi11zyg33 60
320 xp320_y13pmwmp3zy411y0cczcczx226wosr73wc88zyf66zy166 52
360 xp360_xn7zw1bscy4os8zybgn2zoo0u240s4ogkcw33zx342sj2ac 62
368 xp368_y2gy432aczy12251zzggyp62sgz56yc65134w16zyn4o68zy8o8go 48
380 xp380_c4o796zuvvy4sgszc97o4ozx11zyf697o4czy7e2ey4vvuzyfo4o79cz0ck22kcy911z321w123 100
460 xp460_033y133zzzckgsxsgkczzy979102cy733zy9e98043y7ccz31c08zy01050kgzy623 65
480 xp480_y5osq596z4r4y7oy0c871z4r4y6525zy366zy3gggeeezy3333 57
492 xp492_y0o4qa344ozx118f0dc3z8oyago0ab2sycc871z0123y9126e431zy8ooz0mqzyt66w7bcczyy66 87
496 xp496_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2oo0o8i22zy368wov 69
512 xp512_yr33y166z0ggy033y16426ye33y0ccz011w66yuggz66yz56zzzy2mqyz66zygckgk2a21ya66woozy133y0ccye6426y1cczy566y1cc 100
532 xp532_yf697o4czy7sgsy4vvuzyfo4o79czyg11zc4o796zuvvy4e2ezc97o4ozx11y5oky1gcoxoozyerarhhzya35y1163x33 116
690 xp690_0ooy9vtvzyc757zok4sxs4kozzzz033y133 40
836 xp836_y2o8bl46777764lb8ozy311y611zy9aaeyceaazxqmyiggy6ggzy2goye32ql4cssssc4lq23z8kkn9b4303213zx1 115
992 xp992_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zyeggy2gggzwg8keey711xsss333zw1221y022525zy3o8a6 93
1008 xp1008_y48oyc356zy432yi696y9o8gozyjc871zzy12552yg2bq4y4o8zca6y3oggyp113y3ca6zy823ys8kk8zzyogs26zx3123y9cicyi8ozymckoyc32 107"""

rect1 = lt.pattern("""8bo$7bobo$8bo2$6b5o$5bo4bo$4bo2bo$bo2bob2o$obobo5bo$bo2bo4bobo$4b2o2bo
2bo$9b2o9$17b2o$17b2o8$7b2o22b2o$8bo21bo2bo$5b3o23b2o$5bo6$14b2o$15bo$12b3o$12bo""")
rect2 = rect1("rot180",52,74)
grect = lt.pattern("bo$2o$obo")(17,23)

def rectifier_loop(p):
    if p%4 == 0 or p < 106:
        return None
    elif p%4 == 1:
        n_gliders, mpop = (2, 116) if p >= 133 else (10, 156)
    elif p%4 == 3:
        n_gliders, mpop = (6, 136)
    elif p%8 == 2:
        n_gliders = 1 if p >= 266 else 5
        mpop = 113 if p >= 266 else 133 if p >= 210 else None
    else:
        n_gliders, mpop = (3, 123 if p >= 206 else None)
    exts = (p*n_gliders - 266) // 8
    pat = rect1 + rect2(exts,exts)
    for _ in range(n_gliders):
        pat = (pat+grect)[p]
    return (pat, mpop)

p4b1 = lt.pattern("""14b2o$6bo7bo9bo$6b3o3bobo7b3o$9bob3o7bo$8bob2o9b2o$8bo2bo$17bo$16bobo$
9bo2bo2bo2bo$10b2o4b2o$b2o$2bo15b2o$2bobo13bobo$3b2o13bo3$7b2o$6bo2bo$
7bobo$o7bo$3o$3bo$2bo$2bo2bo2b2o$5bo2b2o$3bobo$2bobo$2bo$b2o""")
p4b2 = lt.pattern("""22b2o$22bo$20bobo$18b2obo$15b6o$15b3o$21b2o$21bo$22b3o$16bo7bo$15bobo$
15bo2bo$16b2o3$20b2o$20bobo$22bo$22b2o$7b2o4b2o$6bo2bo3b2o$6bobo$7bo6b
o$14b2o$2b2o12bo$3bo7b2o2bo$3o7bobo3b3o$o9bo7bo$9b2o""")(10,6)

# works down to p36 but fixed oscillators beat it (and it requires more gliders) below p140
def p4_bumper_loop(p):
    if p%8 != 4 or p < 140:
        return None
    exts = (p-140) // 8
    return (p4b1 + p4b2(exts,exts), 141)

mold = lt.pattern("3b3o$bob3o$obobo$o2bo$b2o")(-1,15)

def mold_rectifier_loop(p):
    if p%8 != 4 or p < 212:
        return None
    pat, mpop = rectifier_loop(p//2)
    return (pat+mold, mpop+12 if mpop != None else None)

p8s1 = lt.pattern("""2bo10bo2bo$b3o13bo$3obo13b2o$bo3bo6bob2o6bo$2bo3bo5bo2bo3bo$3bob3o3bo
3bob3o$4b3o3bo11bo$5bo7b3obo3bo$13bo3bo2bo$10bo6b2obo$8bo4b2o$7b2o6bo$
7bobo6bo2bo3$2b2o$bobo$bo$2o""")
p8s2 = lt.pattern("""18bo2bo$17bo$15b2o$12bo6b2obo$b2o4b2o6bo3bo2bo$b2o4b2o6b3obo3bo$12bo
11bo$13bo3bob3o$ob2o3b2o5bo2bo3bo$obo4b2o5bob2o6bo$bo18b2o$b2o16bo$b2o
12bo2bo$b2o""")(9,20)

# 104+8n: Elkies delaying + Handfield–Pierce reflectors; for the latter
# see https://conwaylife.com/forums/viewtopic.php?f=2&t=1437&p=135551#p135546
def p8_shuttle(p):
    if p%8 or p < 104:
        return None
    exts = p//8 - 13
    par = exts%2
    return (p8s1 + p8s2(exts,exts)[4*par], 109+11*par)

snark1 = lt.pattern("""9b2o$8bobo$2b2o4bo$o2bo2b2ob4o$2obobobobo2bo$3bobobobo$3bobob2o$4bo2$
17b2o$8b2o7bo$8b2o5bobo$15b2o7$5b2o$6bo$3b3o$3bo""")
snark2 = snark1("rot90",-20,30)
snark3 = snark1("rot180",10,50)
snark4 = snark1("rot270",30,20)
gsnark = lt.pattern("bo$2o$obo")(7,13)

# only potentially SKOP from p43 to p105 inclusive;
# at periods divisible by 4 is beaten by fixed oscillators
def snark_loop(p):
    mpop = None
    if not (43 <= p < 106 and p%4):
        return None
    elif p%2:
        n_gliders, mpop = (8, 228)
        i = (p-37) // 4 if p%4 == 1 else (p-29) // 2 if p <= 75 else (p-79) // 4
    else:
        if p >= 58:
            n_gliders, mpop = (4, 208)
            i = (p-58) // 4
        else:
            n_gliders, mpop = (8, 230)
            i = (2,3,0)[(p-46)//4]
    slack = p*n_gliders//8 - 29
    pat = snark1 + snark2(-i,i) + snark3(slack-2*i,slack) + snark4(slack-i,slack-i)
    for _ in range(n_gliders):
        pat = (pat+gsnark)[p]
    return (pat, mpop)

p6b1 = lt.pattern("4b2o14bo$2o2b2o12b3o$2o2bob2o9bo$5b3o9b2o2$13bo$5b2o5bobo$5b2o4bo2bo$12b2o")
p6b2 = p6b1("rot90",-2,28)[5]
p6b3 = p6b1("rot180",26,30)[4]
p6b4 = p6b1("rot270",28,2)[3]
gp6b = lt.pattern("2o$obo$o")(14,10)

def p6_bumper_loop(p):
    if p%6 or not p%8 or p < 36:
        return None
    elif p%4:
        n_gliders, mpop = (2, 122) if p >= 66 else (6, 130)
        i = (p-30) // 4 if p <= 54 else 0
    else:
        n_gliders, mpop = (1, 123) if p >= 132 else (3, 127) if p >= 60 else (5, 140)
        i = (1,0,3,6)[(p-36)//24] if p <= 108 else 0
    slack = (p*n_gliders - 124) // 8
    pat = p6b1 + p6b2(-i,i)[2*i] + p6b3(slack-2*i,slack)[2*slack] + p6b4(slack-i,slack-i)[2*(slack+i)]
    for _ in range(n_gliders):
        pat = (pat+gp6b)[p]
    return (pat, mpop)

pd0_1 = lt.pattern("""16b3o$15bo3bo$15bo3bo$16b3o5$16b3o$15bo3bo$15bo3bo$16b3o4$2o3bo2bo3b2o
$5o4b5o$2o3bo2bo3b2ob3o$15bo$16bo""")
pd0_2 = lt.pattern("""6b2o3bo2bo3b2o$6b5o4b5o$6b2o3bo2bo3b2o4$b3o$o3bo$o3bo$b3o5$b3o$o3bo$o
3bo$b3o""")(11,12)

pd15_1 = lt.pattern("""16b3o$15bo3bo$15bo3bo$16b3o5$16b3o$15bo3bo$15bo3bo$16b3o4$2o3bo2bo3b2o
$5o4b5o$2o3bo2bo3b2ob3o$15bo$16bo""")
pd15_2 = lt.pattern("""11b2o$9bo4bo$8bo6bo$7bo8bo$7bo8bo$7bo8bo$8bo6bo$bo7bo4bo$bo9b2o2$bo$ob
o2$3o3$3o2$obo$bo2$bo$bo""")(14,11)
# 30+120n: buckaroo shuttle
pd30_1 = lt.pattern("""o$3o$3bo$2b2o$9b2o$5bo2b2o$4bobo3bo$3bo3bo$3b5o$2b2o3b2o$3b5o$4b3o$5bo
9$4b2o$4b2o""")
pd30_2 = lt.pattern("3b2o$3b2o3$3bo$2bobo$bo3bo$b5o$2o3b2o$b5o$2b3o$3bo8$5b2o$5bo$6b3o$8bo")(13,-11)

pd45_1 = lt.pattern("""17bo$17bo$16b3o3$16b3o$17bo$17bo$17bo$17bo$16b3o3$16b3o$17bo$17bo2$2o
3bo2bo3b2o$5o4b5o$2o3bo2bo3b2ob3o$15bo$16bo""")
pd45_2 = lt.pattern("""7b2o6b2o$6bo2bo4bo2bo$6bo2bo4bo2bo$6bo2bo4bo2bo$7b2o6b2o4$bo$bo$obo$bo
$bo$bo$bo$obo$bo$bo""")(18,19)
# 60+120n: p60 glider shuttle extensions
pd60_1 = lt.pattern("17b3o$2bo2bo4bo2bo3bo$3o2b6o2b3o2bo$2bo2bo4bo2bo")
pd60_2 = lt.pattern("2bo2bo4bo2bo$3o2b6o2b3o$2bo2bo4bo2bo")(25,5)
# 75+120n: 6 bits extensions
pd75_1 = lt.pattern("""20bo$19bobo3$19b3o$19b3o$20bo3$20bo$19b3o$19b3o3$19bobo$20bo$2b2o6b2o$
bo2bo4bo2bo4b3o$6o2b6o3bo$bo2bo4bo2bo5bo$2b2o6b2o""")
pd75_2 = lt.pattern("bo2b2o4b2o2bo$o3b3o2b3o3bo$bo2b2o4b2o2bo")(26,23)
# 90+120n: Elkies–Simkin 1hd reflector with pentadecathlons (p90 version is Silverstream)
pd90_1 = lt.pattern("""7b2o4bo$7b2o3bobo$13bo3$2o2b2o2b2o$2o2b2ob2o$9bo3$3b3o$3b3o$4bo$4bo$4b
o$3bobo3$3bobo$4bo$4bo$4bo$3b3o$3b3o""")
pd90_2 = lt.pattern("""9b3o$9b3o$10bo$10bo$10bo$9bobo3$9bobo$10bo$10bo$10bo$9b3o$9b3o4$9b2o2b
2o$9b2o2b2o3$bo$obo3b2o$bo4b2o""")(13,-2)

def pd_shuttle(p):
    if p%15 or p < 30:
        return None
    q = p//15
    exts, r = divmod(q, 8)
    exts *= 15
    if r == 0:
        return (pd0_1 + pd0_2(exts,exts), 67)
    elif r == 1:
        return (pd15_1 + pd15_2(exts,exts), 75)
    elif r == 2:
        return (pd30_1 + pd30_2(exts,exts), 51)
    elif r == 3:
        return (pd45_1 + pd45_2(exts,exts), 75)
    elif r == 4:
        return (pd60_1 + pd60_2(exts,exts), 29)
    elif r == 5:
        return (pd75_1 + pd75_2(exts,exts), 49)
    elif r == 6:
        return (pd90_1 + pd90_2(exts,exts), 61)
    else:
        return None

# 90+24n: Elkies–Simkin 1hd reflector with p6 thumbs (p114 version is Ocellus)
p6ts1 = lt.pattern("""7b2o4bo$7b2o3bobo$13bo3$2o2b2o2b2o$2o2b2ob2o$9bo3$3b2o$2bo2b2o$2bo4b2o
$2o3bob2o$bobo$bob6o$2bo5bo$3b3o$5bo""")
p6ts2 = lt.pattern("""9bo$9b3o$6bo5bo$6b6obo$11bobo$6b2o2bo2b2o$6bobo2b2o$10bobo$11bo4$9b2o
2b2o$9b2o2b2o3$bo$obo3b2o$bo4b2o""")(13,3)

def p6thumb_shuttle(p):
    if p%24 != 18 or p < 90:
        return None
    return (p6ts1 + p6ts2((p-90)//8, (p-90)//8), 92)

# 98+56n: Elkies–Simkin 1hd reflector with 34P14 shuttles (p98 version is Gallus)
p14_1 = lt.pattern("""12b2o4bo$12b2o3bobo$18bo3$5b2o2b2o2b2o$5b2o2b2ob2o$14bo3$9bo$8b3o$2o4b
2o3bob2o$2o4bo2b2o2b2o$6bob2o4$6bob2o$2o4bo2b2o2b2o$2o4b2o3bob2o$8b3o$9bo""")
p14_2 = lt.pattern("""14bo$13b3o$5b2o4b2o3bob2o$5b2o4bo2b2o2b2o$11bob2o4$11bob2o$5b2o4bo2b2o
2b2o$5b2o4b2o3bob2o$13b3o$14bo4$9b2o2b2o$9b2o2b2o3$bo$obo3b2o$bo4b2o""")(19,0)

def p14_shuttle(p):
    if p%56 != 42 or p < 98:
        return None
    return (p14_1 + p14_2((p-98)//8, (p-98)//8), 105)

# 184+92n: Hickerson's stop-and-go reaction
tbs0_1 = lt.pattern("""2b2o5b2o$2b2o5b2o6$2b3o3b3o$bo2bo3bo2bo$bo3bobo3bo$2obobobobob2o$2ob2o
3b2ob2o$b3o5b3o6$3bo$2bobo$bo3bo$b5o$obobobo$bo3bo2$bo3bo$obobobo$b5o
3b2o$bo3bo3b2o$2bobo$3bo2$2b3o$2bo$3bo""")
tbs0_2 = lt.pattern("""19b2o$18b5o$2b2o14bo4bo5b2o$2b2o14b3o2bo5b2o$19bo2b2o$20b2o$4bo3bo$2b
2obobob2o9b2o$bob2o3b2obo7bo2b2o$o2bo5bo2bo5b3o2bo5b2o$bob2o3b2obo6bo
4bo5b2o$2b2obobob2o7b5o$4bo3bo10b2o""")(-8,10)
tbs92_2 = lt.pattern("""9bo$8bobo$2b2o3bo3bo$2b2o3b5o$6bobobobo$7bo3bo2$7bo3bo$6bobobobo$7b5o$
7bo3bo$8bobo$9bo6$b3o5b3o$2ob2o3b2ob2o$2obobobobob2o$bo3bobo3bo$bo2bo
3bo2bo$2b3o3b3o6$2b2o$2b2o""")(-8,33)

# 138+184n: jslife reflectors-180.lif, 5hd class 1
tbs138_1 = lt.pattern("""b2o5b2o$b2o5b2o13$bo7bo$obo5bobo$3bo3bo$o2bo3bo2bo$bobo3bobo$3b2ob2o$
2ob2ob2ob2o$2o2bobo2b2o$b3o3b3o2b3o$2bo5bo3bo$13bo3$b2o$b2o""")
tbs138_2 = lt.pattern("""3bo$2bobo2$o5bo2b2o$3bo5b2o$2o3b2o4$2o3b2o$3bo$o5bo2$2bobo$3bo3$2bo7bo
$bobo5bobo$4bo3bo$bo2bo3bo2bo$2bobo3bobo$4b2ob2o$b2ob2ob2ob2o$b2o2bobo
2b2o$2b3o3b3o$3bo5bo4$2b2o5b2o$2b2o5b2o""")(21,25)

def twinbees_shuttle(p):
    if p%46 or p < 138:
        return None
    q = p//46
    exts, r = divmod(q, 4)
    exts *= 23
    if r == 0:
        return (tbs0_1 + tbs0_2(exts,exts), 60)
    elif r == 2:
        return (tbs0_1 + tbs92_2(exts,exts), 77)
    elif r == 3:
        return (tbs138_1 + tbs138_2(exts,exts), 72)
    else:
        return None

cfuncs = (rectifier_loop, mold_rectifier_loop, p4_bumper_loop, p8_shuttle, snark_loop,
          p6_bumper_loop, pd_shuttle, p6thumb_shuttle, p14_shuttle, twinbees_shuttle)
