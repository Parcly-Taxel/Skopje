import lifelib
sess = lifelib.load_rules("xsymbiosis")
lt = sess.lifetree()

fixeds = """1 xs2_1_2 2
2 xp2_7 3
3 xp3_f_g 5
4 xp4_ic_1z1 6
5 xp5_ci_1z1 6
6 xp6_s1_w1z1 6
7 xp7_usz1_1z2 7
8 xp8_acs_1zw1 7
9 xp9_02b7_28 7
10 xp10_61e_1 7
11 xp11_02s_21z01 7
12 xp12_22go_1zx1 7
13 xp13_oez1_018z02 9
14 xp14_02208c_410g 8
15 xp15_02b4_4g 7
16 xp16_2og_01z1 6
17 xp17_043h_8hzw1 9
18 xp18_ka4_w12z1 8
19 xp19_9312_g04 8
20 xp20_iem_1z01 8
21 xp21_028s_1zw1 7
22 xp22_028e_4g1 7
23 xp23_2g0cc_1y0gz1 8
24 xp24_030186_2y14 8
25 xp25_2jhx4_1y12zw1 10
26 xp26_2k6_g1 7
27 xp27_05126z01_5g 8
28 xp28_0224c_14xg 8
29 xp29_012413_2w8w1 9
30 xp30_01ee_og 9
31 xp31_giiz01x2_w1z1y14 10
32 xp32_03104_2xgo 8
33 xp33_0g66z2_w1z401 9
34 xp34_2gozwg_1wgz08 8
35 xp35_gx6208_y01x8z1 8
36 xp36_2gq_01z1 7
37 xp37_2oo_1wk 8
38 xp38_024e_18g 8
39 xp39_g09c_x18z1 8
40 xp40_y22z6bh_y21z1zw1 11
41 xp41_0gqw8_w1x4z1 8
42 xp42_03ho_1xg 8
43 xp43_0i974_1y04z1 9
44 xp44_cquz02_01z1 11
45 xp45_0222484_201w2 9
46 xp46_2y22io_4y2102g 10
47 xp47_ja7_c 9
48 xp48_6kz02_018z2 8
49 xp49_waoz4_x1z2x1 8
50 xp50_ha7_a 9
51 xp51_0gk2zy32_w1z1y21 8
52 xp52_06w36z2_4y01z4 10
53 xp53_2wgqb_1y04g 11
54 xp54_2jry1g_1zw1y21 11
55 xp55_079czw1_1g 10
56 xp56_02zcsoz2_w1zw4z4 11
57 xp57_02r9_1x9 10
58 xp58_67ix1_1y21zw1 10
59 xp59_3v15_8x2 9
60 xp60_064076wg_4y010g 11
61 xp61_27az2_x4z1 9
62 xp62_02jr_1zw1 9
63 xp63_4a97_h 10
64 xp64_1318_40g 7
65 xp65_01b4zy81_1gy5g 9
66 xp66_01a4x8_1gy04 8
67 xp67_e96_gw4 9
68 xp68_02sozg_w10oz8 11
69 xp69_063124z8_01y04z08 11
70 xp70_2y2eiu59c_4y5g01 13
71 xp71_sq71z02_1z1 11
72 xp72_2z6cw6_1z8y02 10
73 xp73_01y16c862_1y28y02 12
74 xp74_02bja4_1y0g4 10
75 xp75_hj2zy61_w1y3gz1 10
76 xp76_2jh8x8_1y2gzw1 11
77 xp77_hj2z4_w1z14 10
78 xp78_0ekszg_w10gz8 11
79 xp79_02oozg_w104z8 9
80 xp80_3a17y14_4y34 10
81 xp81_c92qkzy54_10gzy62 13
82 xp82_cmvzw1w8_2zw2wg 13
83 xp83_03w63g_1y0k 10
84 xp84_c96ozy23_10gzy34 13
85 xp85_2jh2xg_1zw1y01 10
86 xp86_01zw26623_2zw4y01 11
87 xp87_rj2y18_w1y1gz1 11
88 xp88_03w63g_1y0c 10
89 xp89_c6wiezw1_2y11zw2 12
90 xp90_0imz411_81z2 10
91 xp91_cm6x2zw1_2y11zw2 11
92 xp92_in2zy21_w1z1y22 11
93 xp93_02y220rd_2y41 10
94 xp94_0cdw5zx1_2w1w2zw2 12
95 xp95_x2jrzg_x1zy11z1 11
96 xp96_0o46z63_k21z8 13
97 xp97_x2z6bh_w1z1zw1 11
98 xp98_0gy2108z0348_gy220gz08g 12
99 xp99_3a7w2_4y12 9
100 xp100_27wro_4y014 11
101 xp101_x1z2ecz1_x2zw2z2 11
102 xp102_x203roz2_x1x4z1 13
103 xp103_06677248_4y01g 12
104 xp104_02so_1x4c 9
105 xp105_245bozz2_1x4zz1 13
106 xp106_06ky12_1y41z01 8
107 xp107_rj2z0g_w1z1z1 11
108 xp108_6ikf9eyc4_g01ye4 13
109 xp109_01z03qg1e_1z04xg 13
110 xp110_0ggx2z19d_gy01zwg 11
111 xp111_67jy34_1y58zw1 11
112 xp112_23pex4_1y28zw1 12
113 xp113_y51z6bh_y62z1zw1 11
114 xp114_g030273_01y04z1 11
115 xp115_67jy24_1y42zw1 11
116 xp116_0239e4z8_01y04z4 13
117 xp117_go4ya2z127_8yb1zw8 12
118 xp118_c92qkzya1_10gzy92 13
119 xp119_hj2y44_w1y48z1 10
120 xp120_2zx6ew6_1zx8y02 11
121 xp121_6bpzy51_1zw1y32 12
122 xp122_hj204_w1w2z1 10
123 xp123_6bhzya1_1zw1y61 11
124 xp124_6i07x1_g01y12 11
125 xp125_01y26c282_1y38y02 11
126 xp126_rj2x2_w1x4z1 12
127 xp127_20ocwo_104y0g 10
128 xp128_rj2zy61_w1z1y52 12
129 xp129_2okex4_4x1x8 10
130 xp130_2zx8pr_1y0gzxg 11
131 xp131_x2z3ucz1_x1zw2z2 12
132 xp132_om26cko_21x248z1 19
133 xp133_63h096y64_1yb2zw1 14
134 xp134_1f0349430f1_g048gw840g 23
135 xp135_1y2kq29c_2y4g01 13
136 xp136_6ikf9ezy64_g01zy68 13
137 xp137_0dcz1_1w4z02 9
138 xp138_036w3z2_04y01z4 10
139 xp139_63jcy51_1y91zw1 13
140 xp140_2jh_1zw1 8
141 xp141_c92qky9g_10gzyd1 13
142 xp142_01wocwo_2x4y0g 10
143 xp143_1zzy3cqi64_2zzy3gy04 13
144 xp144_0gacg04x4zw7rpp_04x8y08x33z18zw1 24
145 xp145_4ogx2zy61_2w8w1xgzzyaoo 14
146 xp146_6bhezy44_1zw1y08 13
147 xp147_y284qa64zz13ybcc_y142w1w2zz04 22
148 xp148_c60246zyb1_2w1w9zya1 14
149 xp149_6bhy21_1y42zw1 11
150 xp150_63pex8_1y2gzw1 12
151 xp151_gv6zy62_w1z1y62 11
152 xp152_6bhzy34_1zw1y14 11
153 xp153_4y3q8gz26y29_8y31w8z8y2802 15
154 xp154_67jy28_1y4gzw1 11
155 xp155_67izw8_1zw18 10
156 xp156_rj2zy38_w1z1y34 11
157 xp157_6bvyb2_1yc1zw1 12
158 xp158_0249he4y31_48gxg8y11 15
159 xp159_rj2zy52_w1z1y34 11
161 xp161_02zxapi84_1zxgy04 12
162 xp162_6bpzy94_1zw1y54 12
164 xp164_01wos0go_1x4y0g 11
165 xp165_cmiya1zw1_2yb1zw2 12
166 xp166_058gzxv96z0a1_10248gzy1g2z80421 25
167 xp167_2jjy14_1y32zw1 11
168 xp168_03ra08zzc4_x1w8zzg 14
169 xp169_63tzy61_1zw1y41 11
170 xp170_03pmzx13yc31_4gzy04yd4 16
171 xp171_6bhzy74_1zw1y58 11
172 xp172_67hy54_1y78zw1 11
173 xp173_6bj_1zw1 10
175 xp175_10brgic_20gy04 14
176 xp176_0o42s8z074zy766_42w124z9zy7802 25
177 xp177_6bvzy88_1zw1y68 12
178 xp178_1zzw3qg18_2zzw4xg 12
179 xp179_wsq6z01y35zy02_04w1y1gz1y5azx2 18
180 xp180_6bh2ey42_1y72zw1 14
181 xp181_6bvy51_1y72zw1 12
182 xp182_0ob3gezz4_04x1zz2 13
183 xp183_63jczy72_1zw1y32 13
184 xp184_cm8y81zw1_2y91zw2 11
185 xp185_rj2zx8_w1z108 11
186 xp186_4w1y258ai48w4_8w2y1106x408 19
187 xp187_0g846y74z1348o_8421y78z48gzx1 22
188 xp188_oi1hzx1ho_2zw1g 15
189 xp189_gosy31z127_8y61zw8 13
190 xp190_6i8b5y54_g01y84 13
191 xp191_63jczy78_1zw1y4g 12
192 xp192_6i8b5y48_g01y74 13
193 xp193_rj2zy52_w1z1y54 11
194 xp194_0ggy51z35c_gy72zwg 12
197 xp197_042176zy91_4y01zy81 12
198 xp198_0cirqcz9876_gzi1 19
199 xp199_c92qky5g_10gzyb1 13
200 xp200_0g865zz2y2g_08x2zz4y28 12
201 xp201_gooy81z124_8ya2zw8 12
202 xp202_y62zcm2zw1_y61z2zw2 11
203 xp203_648085_8g0gw5 12
204 xp204_rj2zy71_w1z1y51 11
206 xp206_rj2zy2g_w1z1y2g 11
208 xp208_6bvy9g_1ya8zw1 12
209 xp209_1ydk8gggzyep9gpmfz8yd21_02yd248zyk6z04yd421 32
210 xp210_hj2z8_w1z18 10
212 xp212_0oaq6yk1z4_041yn1z04 13
215 xp215_o8429248oz4_421x124z2 20
216 xp216_048976zy62_4y01zy74 13
217 xp217_y180s272s08z09yb9zzy51_y08021x1208z9yd9zy5g 26
218 xp218_y22zz0401y1gmczw4x8_y21zwgz4y61z08x4w1 18
219 xp219_203roz4_1x4z8 12
220 xp220_vr2y58_w1y48z1 14
221 xp221_hj2zy14_w1z1y14 10
222 xp222_6bszy12_1zw104 12
224 xp224_6lh6sy04zx1_g8x2x88 19
225 xp225_63jczy68_1zw1y28 13
228 xp228_wsa2z01y35zzx4_04w1y1gz1y5azzw4 17
230 xp230_gosy92z127_8yc1zw8 13
231 xp231_okuz013zy633_w1z1zy84 17
232 xp232_2y1ce248_1y12y08 12
233 xp233_6bhzy766_1zw1y38 14
234 xp234_4auzx28_gw1z014w8 14
235 xp235_63jcy44_1y88zw1 13
237 xp237_0oc463gzy11zw1_8421zwgx21 18
238 xp238_6bhy91_1yc1zw1 11
241 xp241_0ggy61z35c_gy91zwg 12
242 xp242_01zy033z20gz01238y88_w2zz028z14xgy74y166 24
243 xp243_02y9i04kozy9u4qa_2ya1w20gzzy810101 22
244 xp244_c91pmzy92_10gzya4 13
245 xp245_w8ed8gz01xi045zw1_04x248gz1y1ow4z02 26
246 xp246_63h096y54_1ya8zw1 14
247 xp247_063w6z8_01y04z4 10
248 xp248_rj2zx4_w1z1x8 11
249 xp249_2zzw4c972_1zzw8y02 13
250 xp250_6i8b5zzyb8_g01zzycg 13
251 xp251_0p1684zw3y7ggzy08y61_px102zx4zx40gy52 23
252 xp252_2zvqcz1_hzwg 13
253 xp253_hj2zy64_w1z1y48 10
255 xp255_0ok48acylcczy28g0gzzyb31_g02w1zy18zy41zyc4 26
256 xp256_6bhzy2g_1zw1zy21 11
258 xp258_g80ccw2z1azyc4_cx2x1zkzyb2 18
261 xp261_02x8kzw8zw1xeihd1_1z0kz02y481zy31 22
263 xp263_wg144z05w13x4_081w2kz2y32 17
264 xp264_y21zz08gy2azw354_y22zz8y5lz02w8 17
265 xp265_6bvzy64_1zw1y24 12
267 xp267_cmvzw1y08_2zw2xg 14
268 xp268_2yc2zy0124ckkc421_1yc1zx248gy0g842zy41 25
269 xp269_gs21e4z1z01_81x12z0g 16
272 xp272_c92qkzzyc2_10gzzyb2 13
274 xp274_20dbozzy72_1x4zzy64 13
275 xp275_gy11zy33d4cwgz1x8zy42_8y120gzy62x8z01w4zy51 22
277 xp277_0at1ezzy369a4_1y08 17
279 xp279_wg04kpx28gz1011_08x2x1w8z2 18
281 xp281_2z2rp08_1z4xg 13
283 xp283_xob18mz08_x4x1z8 14
284 xp284_gi6tz1x8_8w2zxo 15
285 xp285_01z08y2ma242_1z8y4g01 14
287 xp287_c91pmzzyf2_10gzzye2 13
288 xp288_0goy52z35f_gy71zwg 14
289 xp289_rj2zy41_w1y1gz1 11
290 xp290_14iqg44_2x1084 11
291 xp291_01y0610f7_12x280gwa 16
294 xp294_622ey1433_10gy34 15
295 xp295_0g8meyng02z801yned21_g4x1ym82z082ymgx41 28
298 xp298_2zzw25d932_1zzx8y02 14
303 xp303_0mcz02y18s2zy211_801z5y4g2zy22 20
304 xp304_21252k2zx49ny110c_04x11xgzw8hy5izy01 27
305 xp305_04y3648gz0gy3gg843zy51_4y51248zgy7g81zy621 25
307 xp307_63ty88_1yb8zw1 11
310 xp310_x2jhzz1_x1zy11z2 10
311 xp311_0g86201z124pgy38zwg_842x2z48gy48zxg 24
316 xp316_0ggy71z358_gya1zwg 11
318 xp318_c95uiezyf1_10gydg 17
319 xp319_wgosqqsogz01y41z2y62_g84201w248gzz4y64 25
321 xp321_y41z6bh_y52z1zw1 11
322 xp322_63jczy72_1zw1y51 13
327 xp327_3qh68y24_4xgy28 13
328 xp328_2cpbozzy68_1x4zzy6g 13
332 xp332_08ya204kozyag0g_8yb1w20gzzy910101 16
334 xp334_67jzy31_1y3gzw1 11
337 xp337_hjiwg_w1xgz1 11
340 xp340_wsa2z01y35zz1_04w1y1gz1y5azg 17
341 xp341_0g862y22z124pgzy21_842y45z48gxg 23
343 xp343_04ya24c4ozyag0g_4yb1w20gzzy910101 17
347 xp347_1zz0a40739128zx3w453_2zzly58zy28w2 25
349 xp349_8g2252wkxg_g01x1w8zy71 15
350 xp350_y0gy31y7gz8k6xe48zzx1_y08y41z21y1128y91z1zx2 24
352 xp352_c91pizy51_10gzy62 13
353 xp353_2jrzxg_1zw1zy01 11
356 xp356_gx8c21ac8zyd2zy92_0gw21x124zyc2zy91 20
358 xp358_01zy46d932_1zy48y02 13
362 xp362_2zw5c852_1zw8y02 12
363 xp363_04bj573zg_01y04zz1 18
364 xp364_cmjhd2wg_2y08zy31 18
366 xp366_6bhzy22_1zw1w2 11
383 xp383_okiz011zy91zy4cc_w1z1y8g 16
384 xp384_1zxeiu59c_01zy2g01 13
385 xp385_0ggw1x2z343y1802zzxg_x8w2x1z8y4g02zzzx1 19
387 xp387_zxgz0258vy5252_33z0g8y8gz08gy88zx1 25
388 xp388_8k6xmt2zw1221_21y282z1204w21 24
389 xp389_0g0ca4w1zyc8zz04_w2010402z1ybgzzw4 16
398 xp398_2x125boob521x2_1w248gy0g842w1zy41 25
399 xp399_6i8b5zzy71_g01zzy61 13
408 xp408_02yg1zyj8z0g8gzx352w8_w2ye2zyi4z8zw4080204 20
413 xp413_3qg18wg_4xgzy41 12
415 xp415_2gz640c9_hzw8 12
420 xp420_0g04612zx26ay24_g021x1zw480gy1208 21
424 xp424_0oaq6yl2z4_041ym2z04 13
430 xp430_203ro_1x4 10
437 xp437_0g86601yc4z134ogy38zy08g_842x2yb8z48gy48zy0g 28
446 xp446_06608zy0axhzyc2_4w104zx4gzy51y11 17
456 xp456_2x253zzzybange_4zzzyagy02 19
462 xp462_6i8b5zyh1_g01zyg1 13
469 xp469_c91pmzyhg_10gzzyi1 13
473 xp473_go26y32zx570101_8y521zw28w21 20
475 xp475_3qg18wg_4xgzy21 12
494 xp494_2y54ehne8a4zya1_1yb1g4zy92 21
498 xp498_6bvzy5c8_1zw1y32 14
501 xp501_01zzx8gy2azy0354_1zzw8y5lzx2w8 17
543 xp543_2zzzway2g8zy3453_1zzz0ly58zy38w2 17
545 xp545_ocuy91z013_4ya1zw4 13
555 xp555_67hy38_1y44zw1 11
588 xp588_2y4330m6_1y610g 13
593 xp593_y01zz08gy2azw354_y11zz8y5lz02w8 17
614 xp614_whw1y2oozw4woc2dz4yc1_082x2y34z04y1g02y3gz04y01 25
681 xp681_0g04212y0gzx24e_g021x1y0gzw480g 18
726 xp726_067524zg_01y04z0g 13
781 xp781_y62zyhgz0ooz2zy08zy01x4ige1_y61zzw4yd1z12zxkzx2y481zy51 27
829 xp829_1o6hl6acw1zx111_21y1gx2z01x2 21
921 xp921_4xkwg8ccw42w2zy32x8_22w8y24a0401zy21x4 23
1302 xp1302_0ky4g2zw26454553_62y513z148w88w841 28
2200 xp2200_6i8b5zy48_g01zy3g 13"""

m0small_1 = lt.pattern("11.A$11.B$7.A$6.B2A$AB2$6.A$2.2A2.A.A$2.2A2.2A$3.B")
m0small_2 = lt.pattern("8.B$8.2A$8.2A3$10.BA$3.2AB$3.2A$B$A")(4,6)

m0_1 = lt.pattern("13.2B$2B9.2A.B$B10.2A$.2A$.2A")
m0_2 = lt.pattern("12.A$12.A$12.2A2$13.A$2.2A10.B$B.2A9.2B$2B")(1,8)

m1_1 = lt.pattern("12.A$12.B$8.A$7.B2A2$AB$7.A$7.A.A$2.2A3.2A$2.2A$3.B")
m1_2 = lt.pattern("9.2A$9.2AB3$8.A$8.B$3.2AB$3.2A$B$A")(5,8)

m2_1 = lt.pattern("2.2B$2.B$3.2A$B3.A$.3A2$.B$2.AB")
m2_2 = lt.pattern("BA$2.B2$2.A$2A.B$A$.B$2B")(16,1)

m3_1 = lt.pattern("13.A$13.B$9.2A$8.B2A3$3.B$3.A3$B2A$.2A")
m3_2 = lt.pattern("9.A$9.A$9.2A2$10.A$11.B$10.2B$3.2AB$3.2A$B$A")(4,9)

m4_1 = lt.pattern("13.A$13.B$9.2A$8.B2A3$3.B$3.A3$B2A$.2A")
m4_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(3,9)

m4large_1 = lt.pattern("3.B$4.A$4.2A5.A$10.A$10.3A11$.2A$.2A$B")
m4large_2 = lt.pattern("5.B$3.2A$3.2A13$2A$2A$2.B")(15,3)

m5_1 = lt.pattern("10.B$9.2A$9.2A$13.AB2$3.B$3.A3$B2A$.2A")
m5_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(4,9)

m6_1 = lt.pattern("8.B$7.2A$7.2A$2B9.AB$B$.2A$.2A")
m6_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(2,9)

m7_1 = lt.pattern("13.2B$2B9.2A.B$B10.2A$.2A$.2A")
m7_2 = lt.pattern("10.A$10.A$10.2A2$11.A$12.B$BA9.2B$4.2A$4.2A$4.B")(3,8)

def universal_reflector_loop(p):
    n, r = divmod(p, 8)
    if r == 0:
        if p < 56:
            return None
        elif p < 144:
            return (m0small_1 + m0small_2(n-7,n-7), 32)
        return (m0_1 + m0_2(n-18,n-18), 29)
    elif r == 1:
        if p < 65:
            return None
        return (m1_1 + m1_2(n-8,n-8), 32)
    elif r == 2:
        # there's a p18+8n shuttle akin to Elkies's Life reflector,
        # but it's always beaten by fixed oscillators before p106
        if p < 106:
            return None
        return (m2_1 + m2_2(n-13,n-13), 24)
    elif r == 3:
        if p < 91:
            return None
        return (m3_1 + m3_2(n-11,n-11), 29)
    elif r == 4:
        if p < 84:
            return None
        elif p < 308:
            return (m4_1 + m4_2(n-10,n-10), 29)
        return (m4large_1 + m4large_2(n-38,n-38), 24)
    elif r == 5:
        if p < 85:
            return None
        return (m5_1 + m5_2(n-10,n-10), 29)
    elif r == 6:
        if p < 102:
            return None
        return (m6_1 + m6_2(n-12,n-12), 29)
    else:
        if p < 127:
            return None
        return (m7_1 + m7_2(n-15,n-15), 29)

cfuncs = (universal_reflector_loop,)
