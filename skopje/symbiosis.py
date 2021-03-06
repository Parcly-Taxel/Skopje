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
13 xp13_0330i_1y0h 9
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
25 xp25_2jhw4_1y18z01 10
26 xp26_2k6_g1 7
27 xp27_01x80rm_1y1g 8
28 xp28_0224c_14xg 8
29 xp29_012413_2w8w1 9
30 xp30_01ee_og 9
31 xp31_063w6z1_g1y02 10
32 xp32_03104_2xgo 8
33 xp33_6my18_1y24z1 9
34 xp34_2gozwg_1wgz08 8
35 xp35_gx6208_y01x8z1 8
36 xp36_2gq_01z1 7
37 xp37_2oo_1wk 8
38 xp38_024e_18g 8
39 xp39_g09c_x18z1 8
40 xp40_6jjy0g_1y3gz01 11
41 xp41_0gqw8_w1x4z1 8
42 xp42_03ho_1xg 8
43 xp43_0i974_1y04z1 9
44 xp44_cquz02_01z1 11
45 xp45_0222484_201w2 9
46 xp46_2jhx8_1y24z01 10
47 xp47_ja7_c 9
48 xp48_6kz02_018z2 8
49 xp49_waoz4_x1z2x1 8
50 xp50_6mzy02_1z1y04 9
51 xp51_0gk2zy32_w1z1y21 8
52 xp52_06w36z2_4y01z4 10
53 xp53_6izw3_1z14 9
54 xp54_060272w8_2y010g 11
55 xp55_g063w6_w1y02z1 10
56 xp56_x1z67h_w1z1z01 11
57 xp57_02r9_1x9 10
58 xp58_6iw64_1x1z1 10
59 xp59_3v15_8x2 9
60 xp60_2mzy61_1z1y62 8
61 xp61_3a7zwg_4zz01 9
62 xp62_02jr_1zw1 9
63 xp63_4a97_h 10
64 xp64_1318_40g 7
65 xp65_01b4zy81_1gy5g 9
66 xp66_01a4x8_1gy04 8
67 xp67_e96_gw4 9
68 xp68_6my48_1y64z1 9
69 xp69_1zw36w3_2zw4y02 10
70 xp70_gizw13_1z1x4 9
71 xp71_03h04_1gx8 8
72 xp72_2z6cw6_1z8y02 10
73 xp73_01y16c862_1y28y02 12
74 xp74_02bja4_1y0g4 10
75 xp75_6iy4g_1z1y51 8
76 xp76_06w36z1_2y01z01 10
77 xp77_hj2z4_w1z14 10
78 xp78_23jx8_1y2gzx1 10
79 xp79_02oozg_w104z8 9
80 xp80_3a17y12_4y34 10
81 xp81_w6rwuz1_w1y02z2 11
82 xp82_2jrzy12_1z01y02 11
83 xp83_6mw4_1y02z1 9
84 xp84_2y5edhe_1y41y08 13
85 xp85_01xcowc_1y0gy08 10
86 xp86_0130e_2xg4 9
87 xp87_2jh8x4_1y34z01 10
88 xp88_03w63g_1y0c 10
89 xp89_2y18gie_1y0gy02 11
90 xp90_0imz411_81z2 10
91 xp91_cm6x2zw1_2y11zw2 11
92 xp92_y42z2jh_y51z1z01 10
93 xp93_02y220rd_2y41 10
94 xp94_0gy51z199_gy71z0g 10
95 xp95_067w6z02_01y02z2 11
96 xp96_occx1z172_4y12zx4 12
97 xp97_67jy18_1y34z01 11
98 xp98_1wcwoc_208y0g 10
99 xp99_3a7w2_4y12 9
100 xp100_2jhzy11_1z01x2 10
101 xp101_063074z8_01y08z0g 11
102 xp102_hj2w8_w1x4z01 10
103 xp103_3a17y32_4y51 11
104 xp104_02so_1x4c 9
105 xp105_3a7y22_4y31 9
106 xp106_06ky12_1y41z01 8
107 xp107_kkezw2_x1z14 10
108 xp108_2zxco464_1zxgy08 11
109 xp109_1x40ooc_2w8y0g 11
110 xp110_0ggx2z19d_gy01zwg 11
111 xp111_67jy34_1y58zw1 11
112 xp112_23pex4_1y28zw1 12
113 xp113_02y142is_1y12y0g 11
114 xp114_g030273_01y04z1 11
115 xp115_2nizy32_1z01y24 11
116 xp116_2niy18_1y3gz01 11
117 xp117_23tk8_1y0gz01 11
118 xp118_67hy18_1y2gz01 11
119 xp119_hj2y44_w1y48z1 10
120 xp120_2zzw36w3_1zzw4y02 10
121 xp121_cu1x2zw1_2y21z02 12
122 xp122_1080oo_2gy0g 9
123 xp123_6bhzya1_1zw1y61 11
124 xp124_6i07x1_g01y12 11
125 xp125_27jy21_1y32zx1 11
126 xp126_67hzy28_1z01y1g 11
127 xp127_6qczy12_1z1y04 10
128 xp128_rj2zy61_w1z1y52 12
129 xp129_6iwf_1y0gz1 9
130 xp130_2zx8pr_1y0gzxg 11
131 xp131_x2z3ucz1_x1zw2z2 12
132 xp132_ci26y22_x1y14z1 11
133 xp133_02y242is_1y22y0g 11
134 xp134_suzzzy42_1z1zzy34 10
135 xp135_6my16s_1z1y31 12
136 xp136_6ikf9ezy64_g01zy68 13
137 xp137_0dcz1_1w4z02 9
138 xp138_036w3z2_04y01z4 10
139 xp139_63jcy51_1y91zw1 13
140 xp140_2jh_1zw1 8
141 xp141_c92qky9g_10gzyd1 13
142 xp142_01wocwo_2x4y0g 10
143 xp143_1zzy3cqi64_2zzy3gy04 13
144 xp144_ciq6zy4g_x1z1zy51 12
145 xp145_omczy42_1z1y24 10
146 xp146_okuwg_x1wgz1 10
147 xp147_g3304_1y08z1 9
148 xp148_c60246zyb1_2w1w9zya1 14
149 xp149_2aiczzy61_1zx1zy72 11
150 xp150_63pex8_1y2gzw1 12
151 xp151_gv6zy62_w1z1y62 11
152 xp152_6bhzy34_1zw1y14 11
153 xp153_1zx6wc6_2zw4y08 10
154 xp154_67jy28_1y4gzw1 11
155 xp155_67izw8_1zw18 10
156 xp156_rj2zy38_w1z1y34 11
157 xp157_6btzy1g_1z01y08 12
158 xp158_0249he4y31_48gxg8y11 15
159 xp159_2g4gco_1y04z1 11
160 xp160_6blzy22_1z01y01 12
161 xp161_02zxapi84_1zxgy04 12
162 xp162_2btex4_1y22zx1 10
164 xp164_01wos0go_1x4y0g 11
165 xp165_cmiya1zw1_2yb1zw2 12
166 xp166_2jmzzy11_1z01zy12 11
167 xp167_2jrzy2g_1z01y08 11
168 xp168_x1zabv_y02z1z01 12
169 xp169_1zw6wc6_2z04y08 10
170 xp170_03pmzx13yc31_4gzy04yd4 16
171 xp171_6bhzy74_1zw1y58 11
172 xp172_67hy54_1y78zw1 11
173 xp173_6bj_1zw1 10
175 xp175_2wco02c_1wgy08 11
176 xp176_2zce2zw1_1z2z02 11
177 xp177_6bvzy88_1zw1y68 12
178 xp178_1zzw3qg18_2zzw4xg 12
179 xp179_c5ewg_2zy21 9
180 xp180_6bh2ey42_1y72zw1 14
181 xp181_6bvy51_1y72zw1 12
182 xp182_2jrz0g_1z01z1 11
183 xp183_2tv6z8_x1zg01 12
184 xp184_gqiz01y62_01z1y84 11
185 xp185_euzy44_1z1y42 10
186 xp186_4w1y258ai48w4_8w2y1106x408 19
187 xp187_ci2qszyag_x1z1y88 14
188 xp188_oi1hzx1ho_2zw1g 15
189 xp189_gosy31z127_8y61zw8 13
190 xp190_2jiy22_1y54z01 10
191 xp191_63jczy78_1zw1y4g 12
192 xp192_6i8b5y48_g01y74 13
193 xp193_rj2zy52_w1z1y54 11
194 xp194_0ggy51z35c_gy72zwg 12
195 xp195_0hb6x4_x1y04z1 10
197 xp197_042176zy91_4y01zy81 12
198 xp198_oqzzwg_1z1zx8 9
199 xp199_c92qky5g_10gzyb1 13
200 xp200_0g865zz2y2g_08x2zz4y28 12
201 xp201_gooy81z124_8ya2zw8 12
202 xp202_y62zcm2zw1_y61z2zw2 11
203 xp203_648085_8g0gw5 12
204 xp204_27jzy11_1zx12 11
206 xp206_rj2zy2g_w1z1y2g 11
207 xp207_y36d9ez1_gy11y08 14
208 xp208_6bvy9g_1ya8zw1 12
209 xp209_4c4x33z0gz35e_y14zgz0g 19
210 xp210_hj2z8_w1z18 10
212 xp212_0oaq6yk1z4_041yn1z04 13
213 xp213_02y18sje_4y1gy02 13
214 xp214_y51z2jh_y62z1z01 10
215 xp215_o8429248oz4_421x124z2 20
216 xp216_1y24897_2y18y01 11
217 xp217_2jhzzy3g_1z01zy38 10
218 xp218_27jy24_1y54zx1 10
219 xp219_203roz4_1x4z8 12
220 xp220_vr2y58_w1y48z1 14
221 xp221_hj2zy14_w1z1y14 10
222 xp222_6bszy12_1zw104 12
224 xp224_6lh6sy04zx1_g8x2x88 19
225 xp225_63jczy68_1zw1y28 13
226 xp226_2jmzzy6g_1z01zy78 11
227 xp227_0259d6zya1_4y08zy91 14
228 xp228_wsa2z01y35zzx4_04w1y1gz1y5azzw4 17
229 xp229_01zy3ehde_1zy28y01 13
230 xp230_cia64y22_x1y21z1 13
231 xp231_okuz013zy633_w1z1zy84 17
232 xp232_2y1ce248_1y12y08 12
233 xp233_01wmq28_2y1g 11
234 xp234_4auzx28_gw1z014w8 14
235 xp235_63jcy44_1y88zw1 13
237 xp237_2jhzzy82_1z01zy94 10
238 xp238_6bhy91_1yc1zw1 11
241 xp241_0ggy61z35c_gy91zwg 12
242 xp242_hj2zz1_w1z01z2 10
243 xp243_4qqiczya4_01zy01y62 14
244 xp244_c91pmzy92_10gzya4 13
245 xp245_y11z2jhe_y01z1z01 13
246 xp246_63h096y54_1ya8zw1 14
247 xp247_063w6z8_01y04z4 10
248 xp248_3a7y5g_4zy91 9
249 xp249_2zzw4c972_1zzw8y02 13
250 xp250_0g8y01z55f_gy12zxg 12
251 xp251_goezy3g_x1z1zy31 10
252 xp252_2zvqcz1_hzwg 13
253 xp253_hj2zy64_w1z1y48 10
255 xp255_01zcimo_w1z1zx1 13
256 xp256_6bhzy2g_1zw1zy21 11
258 xp258_g80ccw2z1azyc4_cx2x1zkzyb2 18
260 xp260_2jhzzy18_1z01zy1g 10
261 xp261_2nizzy21_1z01zy12 11
262 xp262_020cc6y61_4y08y51 11
263 xp263_wg144z05w13x4_081w2kz2y32 17
264 xp264_1zz06bt_2zz01zw1 13
265 xp265_0h3284_x1w8z1 10
267 xp267_cmvzw1y08_2zw2xg 14
268 xp268_2yc2zy0124ckkc421_1yc1zx248gy0g842zy41 25
269 xp269_gs21e4z1z01_81x12z0g 16
271 xp271_2nizy82_1z01y61 11
272 xp272_c92qkzzyc2_10gzzyb2 13
273 xp273_2jio8ggzxedlj_1z01y1g 18
274 xp274_20dbozzy72_1x4zzy64 13
275 xp275_i2icz11x4_1zx102 13
276 xp276_cigozy44_1zx1y08 11
277 xp277_2jhzy04_1z01x2 10
279 xp279_wg04kpx28gz1011_08x2x1w8z2 18
280 xp280_2jizyc1_1z01y91 10
281 xp281_2z2rp08_1z4xg 13
283 xp283_2nizz01_1z01zw1 11
284 xp284_27206zybg_1y02zyc8 11
285 xp285_01z08y2ma242_1z8y4g01 14
286 xp286_4ajheezzx1_01zw1zw1 18
287 xp287_2jhezy74_1z01y68 12
288 xp288_0goy52z35f_gy71zwg 14
289 xp289_2jhzyc1_1z01yb1 10
290 xp290_14iqg44_2x1084 11
291 xp291_01y0610f7_12x280gwa 16
292 xp292_2niy31_1y52z01 11
294 xp294_622ey1433_10gy34 15
295 xp295_06jlezz4_01zw1z8 15
297 xp297_cikm4zy81_1zx1y52 14
298 xp298_2zzw25d932_1zzx8y02 14
299 xp299_2jmzzy21_1z01y1g 11
300 xp300_0hb6zzy71_x1z1zy72 11
301 xp301_063124z8_01y08zg 11
303 xp303_0mcz02y18s2zy211_801z5y4g2zy22 20
304 xp304_21252k2zx49ny110c_04x11xgzw8hy5izy01 27
305 xp305_04y3648gz0gy3gg843zy51_4y51248zgy7g81zy621 25
307 xp307_63ty88_1yb8zw1 11
308 xp308_2jhzzy41_1z01zy42 10
310 xp310_x2jhzz1_x1zy11z2 10
311 xp311_0gy11z198t_gy11z0g 13
316 xp316_0ggy71z358_gya1zwg 11
317 xp317_2nizzw4_1z01z04 11
318 xp318_c95uiezyf1_10gydg 17
319 xp319_wgosqqsogz01y41z2y62_g84201w248gzz4y64 25
321 xp321_y41z6bh_y52z1zw1 11
322 xp322_63jczy72_1zw1y51 13
325 xp325_cihjzy52_1zx1y21 13
326 xp326_c91pmzy5102_10gzy62 14
327 xp327_w63w6z1_w1y08z2 10
328 xp328_2cpbozzy68_1x4zzy6g 13
329 xp329_02xe19m_2x8y01 13
330 xp330_2jhha4y24zy73_1y72z01 17
332 xp332_w1zcilh1a4_01z1zx1 15
334 xp334_67jzy31_1y3gzw1 11
337 xp337_hjiwg_w1xgz1 11
340 xp340_wsa2z01y35zz1_04w1y1gz1y5azg 17
341 xp341_0g862y22z124pgzy21_842y45z48gxg 23
343 xp343_04ya24c4ozyag0g_4yb1w20gzzy910101 17
346 xp346_4erlezzy71_gy02zzy61 15
347 xp347_1zz0a40739128zx3w453_2zzly58zy28w2 25
349 xp349_8g2252wkxg_g01x1w8zy71 15
350 xp350_y0gy31y7gz8k6xe48zzx1_y08y41z21y1128y91z1zx2 24
352 xp352_2jhy58_1y6gz01 10
353 xp353_01zx4cc33_2zx8y04 11
356 xp356_gx8c21ac8zyd2zy92_0gw21x124zyc2zy91 20
358 xp358_01zy46d932_1zy48y02 13
362 xp362_2zw5c852_1zw8y02 12
363 xp363_04bj573zg_01y04zz1 18
364 xp364_cmjhd2wg_2y08zy31 18
366 xp366_6bhzy22_1zw1w2 11
367 xp367_2nizzy71_1z01zy61 11
368 xp368_4ejjzy6cc_01zw1y22 16
370 xp370_2nizzy84_1z01zy94 11
374 xp374_2zy2co0k4_1zy2gy08 11
379 xp379_02y66bpic_1y71y02 15
382 xp382_0e1tazzyb2_8y01zzyc4 12
383 xp383_0e1tazzyc2_8y01zzyb2 12
384 xp384_1zxeiu59c_01zy2g01 13
385 xp385_0ggw1x2z343y1802zzxg_x8w2x1z8y4g02zzzx1 19
386 xp386_2jhezy3g_1z01zy41 13
387 xp387_zxgz0258vy5252_33z0g8y8gz08gy88zx1 25
388 xp388_y4635c4z1zoo_0gy21y02 17
389 xp389_0g0ca4w1zyc8zz04_w2010402z1ybgzzw4 16
390 xp390_ciq6zzy9g_x1z1zy8g 13
396 xp396_0e1tazzyc1_8y01zzyb1 13
397 xp397_0e1tazye4_8y01zyf2 13
398 xp398_2x125boob521x2_1w248gy0g842w1zy41 25
399 xp399_6i8b5zzy71_g01zzy61 13
403 xp403_0hb6zyb1_x1z1yb1 11
404 xp404_cihjzy48_1zx1xg 13
408 xp408_02yg1zyj8z0g8gzx352w8_w2ye2zyi4z8zw4080204 20
413 xp413_3qg18wg_4xgzy41 12
415 xp415_2gz640c9_hzw8 12
420 xp420_0g04612zx26ay24_g021x1zw480gy1208 21
423 xp423_0e1tazycg_8y01zybg 14
424 xp424_0oaq6yl2z4_041ym2z04 13
430 xp430_203ro_1x4 10
431 xp431_2jhzzy38_1z01zy44 10
437 xp437_0g86601yc4z134ogy38zy08g_842x2yb8z48gy48zy0g 28
444 xp444_ciaq8zzyb8_x1z1zya8 14
446 xp446_06608zy0axhzyc2_4w104zx4gzy51y11 17
448 xp448_y8239ez2_y71y08z4 12
455 xp455_y9at1ez2_y81y08z1 12
456 xp456_0e1tazyqg_8y01zyp8 14
459 xp459_6jhez04_1z018 13
462 xp462_6i8b5zyh1_g01zyg1 13
469 xp469_c91pmzyhg_10gzzyi1 13
473 xp473_go26y32zx570101_8y521zw28w21 20
475 xp475_3qg18wg_4xgzy21 12
476 xp476_0e1tazzyg8_8y01zzyh8 13
478 xp478_ci26zzyag_x1z1zyb8 11
481 xp481_yb659ez1_gy91y08 13
488 xp488_01zygange_1zyfgy02 14
490 xp490_2mqcz01x2_1zx14 13
494 xp494_2y54ehne8a4zya1_1yb1g4zy92 21
498 xp498_6bvzy5c8_1zw1y32 14
501 xp501_01zzx8gy2azy0354_1zzw8y5lzx2w8 17
510 xp510_cihhezy82_1zx1y34 14
513 xp513_6qiczy18_1zx14 13
519 xp519_cimozy82_1zx1y44 13
525 xp525_02zyc7b97_1zyb8y01 14
528 xp528_27206zyb2_1y02zyb4 11
533 xp533_cihhzy664_1zx1y44 14
543 xp543_2zzzway2g8zy3453_1zzz0ly58zy38w2 17
545 xp545_ocuy91z013_4ya1zw4 13
555 xp555_67hy38_1y44zw1 11
561 xp561_yjat1ez8_yi1y08z4 13
585 xp585_27jzyb2_1zx1y81 11
588 xp588_2y4330m6_1y610g 13
593 xp593_y01zz08gy2azw354_y11zz8y5lz02w8 17
598 xp598_cihhzy5c4_1zx1y34 14
614 xp614_whw1y2oozw4woc2dz4yc1_082x2y34z04y1g02y3gz04y01 25
681 xp681_0g04212y0gzx24e_g021x1y0gzw480g 18
717 xp717_2jry84_1yb4z01 11
726 xp726_067524zg_01y04z0g 13
781 xp781_y62zyhgz0ooz2zy08zy01x4ige1_y61zzw4yd1z12zxkzx2y481zy51 27
829 xp829_1o6hl6acw1zx111_21y1gx2z01x2 21
873 xp873_2jry5g_1y78z01 12
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

# pat = lt.pattern("A.A$A.A$A2.B$.AB")
# print(pat.period, pat.apgcode, minpop(pat))
# qat = skop(pat.period, "symbiosis")[0][0]
# print(qat.apgcode, minpop(qat))
"""
newfixed = {}
f1 = fixeds.split("\n")
with open("nosc", 'r') as f2:
    for (priority, f) in enumerate((f2, f1)): # f2 over f1
        for l in f:
            p, apg, mp = l.split()
            p = int(p)
            tentative = (int(mp), priority, apg)
            existing = newfixed.get(p, (9999, 9999, 9999))
            if tentative < existing:
                newfixed[p] = tentative
for (p, (mp, _, apg)) in sorted(newfixed.items()):
    print(p, apg, mp)
"""
