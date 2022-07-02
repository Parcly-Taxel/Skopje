import lifelib
sess = lifelib.load_rules("b3s23")
lt = sess.lifetree(n_layers=1)

fixeds = """1 xs4_33 4 block
1 xs4_252 4 tub
2 xp2_7 3 blinker
3 xp3_4hh186z07 12 caterer
4 xp4_37bkic 12 mold
4 xp4_ssj3744zw3 12 mazing
5 xp5_y2g0k413zwo0a02z32 15 pseudo-barberpole
6 xp6_ccb7w66z066 16 unix
7 xp7_0g88b5oz1255kk3033zy011 28 burloaferimeter
7 xp7_o8bbc0sz017871x31e8 28 28P7.1
7 xp7_o8y2gbdz0dl31w11156z011 28 28P7.2
7 xp7_5b8b94gszw652y06a8o 28 28P7.3
8 xp8_gk2gb3z11 12 figure eight
9 xp9_0c93wmk46z69bo7421 29 29P9
10 xp10_c846l3wszy03wca6213 24 24P10
11 xp11_y0dbzggci5ld3xog8oz0343 33 rattlesnake
12 xp12_032acy0oge2z0g8ow77ggz23y21226 33 dinner table
13 xp13_gy1gr3zd5a64210g8c4066zy2kr6og 34 Beluchenko
14 xp14_j9d0d9j 16 tumbler
15 xp15_4r4z4r4 12 pentadecathlon
16 xp16_0c2w3vz33032988 21 Rob
17 xp17_32acy1ca23zy27rszwo8a6y16a8o 36 honey thieves
18 xp18_66625ak8zy177xcc0cczy1g8mwiozx91gp 43 H(bi-block)
18 xp18_wc93xs112ogggzbdhe96kk801zw1213 43 PS(3*5+3,3)
20 xp20_35426ow37bkicz65123 30 LCM(4,5)
21 xp21_g8gw3jz01xqpwsszy111wc2w8k8zy566 32 Ø
22 xp22_178cwggg2y2oo4kozy235433y28111w62sg 36 Jason
23 xp23_0ggw32acxca23wckzgg346xoo8ggy065loz1qa6y2111x62sgz023wc453x354c 76 H(HF)
24 xp24_xsssx4hh186z777y37 24 LCM(3,8)
25 xp25_32aczy0ooj64zy74cp33zyc6a8o 30 30P25
26 xp26_0c4o796kcimkk8goz4aajkm0fomi87kggzca245l4870122c543zy111 87 LCM(2,13)
27 xp27_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910oo 56 56P27
28 xp28_033y133zo4maxam4oy1ggz1ppy1pp1xsta43 46 LCM(4,14)
29 xp29_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11zzy8252y1252 54 PPS
30 xp30_w33z8kqrqk8zzzw33 20 queen bee shuttle
31 xp31_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066 48 Merzenich
32 xp32_wosq596zy3oy0c871zy2525z66zgggeeez333 45 H(HF)
33 xp33_8ehe8oy1o8a6zw12ll64x88c04c6ezy056y313 46 LCM(3,11)
35 xp35_y4ok46y3253zooxgcgy47r4xcczxgw33y0ggkczw321y31 44 H(HF)
36 xp36_32aczy08c8y0131zya354c 22 22P36
37 xp37_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354c 58 H(R)
38 xp38_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7 44 roc
39 xp39_xqh2z33173xccz4sk0emicy2oozy469dezy4327 46 LCM(3,13)
40 xp40_33zxs48g69gvzx3021zy833 26 Beluchenko
42 xp42_033y133zo4maxam4oz1ppy1pp1xgfnzyb1252333 50 LCM(6,14)
44 xp44_0oql96xmqzgh1gxeqaa4oz1011y217871 45 LCM(4,11)
45 xp45_vtvy2j9e0o4cz757y1ojhrhla23zy666 48 LCM(9,15)
46 xp46_033y133zzzckgsxsgkczz0cc 28 twin bees shuttle
47 xp47_w32acyeca23zy37y2ccy27z252xeaey8eaex252zg8gxsksy8sksxg8gz01y1oy2ccy2oy11zwggkc01ya10ckggzw1yk1 84 PPS
48 xp48_660259gcy1g8gzy166y1sspxgk2gb3zy8ooy011 44 LCM(6,16)
49 xp49_yzylc69h1hm4k8zyzyb8gy34b8q3034odzyzy972qngy61111g0s82u08k8zyzwsg8y4ggy488oxcc011w11zyzy76221y51zyqgzyo132yf532zyqgzy7ooxca8y46511y284sz8k80u28s26ya4kc0gzy011woci222c88gy37913zy38mgk7079grzy6122221 188 p7 22hd reflector loop
50 xp50_y132aczy5ooj64zwg08oy64cp33z320i9802i908oy46a8ozy33201 58 LCM(10,25)
51 xp51_g08o0u15gis89f0s48cz11wdbaik68jd0ddy1ca23zy232011y1sr7zy6o8a6y16a8o 90 LCM(3,17)
52 xp52_4s0gy3ca23zw11w4ed3zy08oy362sgzw311 35 H(LOM)
54 xp54_32acy5ca23zy1ooxoozx4ossxsso4zzzc453y5354c 48 p54 shuttle
55 xp55_y0dby06a8gzggci5ld3xogg150cgz0343y523y0346 49 LCM(5,11)
56 xp56_66625dw66zyb66zzy0oow8s26zy61ooo8kkwoozyc1 45 p56 B-heptomino shuttle
57 xp57_yzylg2tugzyzykof0cs7zyzyb8e96y21130186y0ggzyzyc117y8gg0643zyzw654y4o8a6y184sy211zzzyn361yd86czzy9gy6gzy1ooy2321y16511y42a6zgs26ybe88zy2618gc88gy16971zy4ujj0v1zy57b4 146 p3 22hd reflector loop
58 xp58_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cc 54 H(pi)
60 xp60_vtvy037bkicz757 24 LCM(4,15)
62 xp62_ccy069c536635c96y0cczz66y0ci6koccok6icy066zzy4ojd11djo 66 PS(5*12+2,31)
63 xp63_06e1044im4k8z04b8ri8810tozy4ghz354mgv2r0v066zw3204701 74 LCM(7,9)
64 xp64_y1j3zy031d8ey633zggy6s4c0gz11y8hj1zya11 34 Merzenich
65 xp65_3pmwmp3zxh1gx21h2zx3c7a5301gk2w96zy5admlk 52 LCM(5,13)
66 xp66_y2ca23zws21q4zx11zxgc22szw8o121z311y0681hh4zy77 48 LCM(3,22)
68 xp68_w32acy1ca23zy2sr7zo8a6y1mm0mp2c82u08ozy51qaic0d5521 72 LCM(4,17)
69 xp69_y4gut2gzy47sc0fozggy06810311z0346xgg8ooy14aa4y3562zy51y76a8ozzykgoyfgkozyk101zzzyzw6a2ye163zzyzyl64kozyzyfgo8y38kk8y166522xo8gzyzyh1ydgw4oy032zyzyw6t1depzyzyx3geu3zyzyz1 146 p3 22hd reflector loop
70 xp70_033y133y1o62453zo4maxam4oy132156z1ppy1pp1 52 LCM(5,14)
72 xp72_3bg2kgzy011y7ok46zy268ga4w8k24ozxo8a6 36 LCM(8,36)
74 xp74_y532acy5ca23zggyrggz0346y5636404636y5643zz0o4cy5coc404cocy5c4oz11yr11zy5o8a6y56a8o 84 Raucci
75 xp75_32aczy0ooj64zy74cp33zyc6a8ozy288k8888k88 46 LCM(15,25)
76 xp76_o4an7y1ca23yi32acz0110888xooxoa6ya6aoxoox888zy47ys7 56 LCM(4,38)
77 xp77_ok4miewm9azk4q11sjr8a6zg1ggy2gs2sgz1101xebaa43zy5db 71 LCM(7,11)
78 xp78_y45rc31zwmkac48g012640cczw1wgw1rozmkgino3s4z1w6221 61 LCM(6,13)
80 xp80_35426ox22i8o0ooz65123y1vow86 39 LCM(5,16)
81 xp81_yzyzwca23zyzyy33y2eu80gswsg0gzyzyw2a6y4178ewew121zyzyz0o4ozyzyugs26x1zyzyzxco4zyzyca64zzzyzyisg8zyu42ezzzyz08okzya86czyhoge2zyc696z0gxsws4oy5okgz1212ewe205vsy2ggzyaggkc011zya1 146 p3 22hd reflector loop
84 xp84_8oymca23z0123ya4995zy9kii4yao8gzxo8a6ym32 42 H(HF)
85 xp85_w32acy1ca23zy2sr7zo8a6y1mm0mp3c48cggzy5122m031fhd221zy811 74 LCM(5,17)
87 xp87_ya32aczyfg8gw33y466zxg8gy81221zggw1oogyesscz11y2deeyd1266x33zycggy9252z0ooy4ggw3421zy711y2ckggzyi1 84 84P87
88 xp88_3bg2kgzy011y1o4oz3213xgonl9611zy5qm 45 LCM(8,11)
90 xp90_w33z8kqrqk8zy6cczy43llhhla8ozw33y1pie0346 56 LCM(9,30)
91 xp91_g8e1qiga64oy0oggz78ok2im0s43xsd4pzy31w66x110ciqs0ae8zyccc 72 LCM(7,13)
92 xp92_66yb7pe4y266xoozooybo6s8y99ecsgzyd11y9oib3 49 LCM(4,46)
93 xp93_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy44hh186zy57 60 LCM(3,31)
94 xp94_x696o8b9czy065x33xc871xggzooyd643zwgg04ahhha4y5c871z4701yfoozw8e13xggzy34701xmmggo5jzya146w343 110 capgun
95 xp95_gwg6t1e8gz11dlka211feow8gzy38o0122221zy41230oows48y12552y7g0gzyo354cy431zzzzyz46ayhgkozzzzzyzyk351yhac4zzzzyzyzy5goy464kozyzyzy5101y78kk8y1247w330o8gzyzyzyvg8888g032zyzyzyv12w3eugg8a5lmggzyzyzyzw12egnc1w1 166 p5 22hd reflector loop
96 xp96_0178cy766zy44koy6m640ooe4a4z0gs26x11xoy1oo022440ezo8go 59 capgun + boat-bit
99 xp99_8oy3nl6z0123ws21913z8e13x12mmjy3mqzy53210gxeqaa4ozy66511y217871 82 LCM(9,11)
100 xp100_32aczy0ooj64zg88gy34cp33z125eey76a8o 42 LCM(4,25)
102 xp102_ybc453zyeg8w4kk8y2gg8kbw9czy1ooy678c48by5408czooog8lb4zy01yeggozyi32 67 Raucci
104 xp104_gk2gb3y013cr5z11y0cc046210g84cakmzy8or1y11 46 LCM(8,13)
105 xp105_0oggxooy1vtvzc88m5o0ccy1757zw1qm0f952 49 LCM(7,15)
108 xp108_wc4o0oy6g033zougdb158cy1a9871zy0ooyf789q8zy42bi2syf33zyfgs2iazydoo01 78 LCM(4,27)
110 xp110_c4oy1178cwggg2y2oo4kozx160kgy235433y28111w62sgzy412ac 51 LCM(5,22)
112 xp112_om999e0e999mozx8kc0ck8zzw8if505fi8 50 LCM(14,16)
113 xp113_y98oyn33y166z8oy732ys33y0ccz01219g8y2gkszwcq2qbyzy18e1eozx121ywsk4y2b591zxooyzy5221e8zy3gg33ysdbzy311y133 106 nihonium
114 xp114_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zye4hh186zyf7 57 LCM(3,38)
116 xp116_y6o4an7zy711zy166y5ok4kozym31e8zx32acyc6a8oz2egozy535453y5cc 68 LCM(4,58)
117 xp117_x32acxca23zggxg84448gxggy2g88cz14fes72x27sef41y211zyfeehrzyq33zyfo8gy5g33zyfopw11267608g3568w66zyseu4zyu3 112 LCM(9,39)
120 xp120_4r4y13bg2kgz4r4y511 24 LCM(8,15)
124 xp124_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy337bkic 60 LCM(4,31)
126 xp126_0ccy1ccx32acxca23zcmkgxgkmcy24r4zy0202y64r4z033y133xo8a6x6a8o 74 LCM(9,14)
128 xp128_y3ca73oswcczyqg88gzy1ggyh6bbcxca4z8ko010onmcy04eewuscy26dt30g0352z4a6x6qqcyh11zy01221zyh66w73osa6 108 H(wing)
129 xp129_yzyzyzy7ca23zyzyzyzy4jjy2eu80gswsg0gzyzyzyzy3103y3178ewew121zyzyzyzy6o4ozyzyzyzy0gs26x1zzzzyzyzya86cyg265zzzzzzyzyhgggygokgzyzyi21zzzzzzyoa64yg361zzzyjggzycg8gw643zyc121z8k8gg70gn1eoy3sg8zy03w3w177y2cczyac453 146 p3 22hd reflector loop
130 xp130_og8o0u1eozy0mlgrzx1qa2my2meiz62460v0t60gg037fa60ggzy21x11y236fe5267zyc33 89 LCM(10,13)
132 xp132_252w253zy0gxggg0ooozy13w3488a61oml1hiswcgzw695qsoy3111zyica4w4a4 72 LCM(4,33)
135 xp135_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910ooy2uquzyjfbf 68 LCM(15,27)
138 xp138_w8gw259r84z79431y1go4iszx42rik8w12 36 Gabriel
140 xp140_033y133zo4maxam4oy1gy1gs26z1ppy1pp1y0121ggcaaq552zy8ok46o7o7421zyd1 82 LCM(14,20)
141 xp141_y64a4y14a4w178cx8e1e8gzy2sy0cscxcscy0sx33159d11z8e13yj31e8z8oy133y933y1o8z0123wsy0osoxosoy0sw321zy6g8gy1g8gzy71y31 114 PS(7*20+1,47)
143 xp143_0gs2ibaa4y5o8zlm0mlluy2sse321wbdz25s16a98gxo8gox13tlicggzx11311yb343 99 LCM(11,13)
144 xp144_33y18kk8yb33zy8equzy9757wggzccyb1221y1cc 42 Achim
150 xp150_w178cxg8zy417gukzy75f1sgzccb7w66y121x62sgz066 46 LCM(6,25)
152 xp152_32acywca23zwsy48kie4y84eik8y4szy1771yo177zybgggeeezyb333 60 LCM(8,38)
155 xp155_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2idiidizy31w1 64 LCM(5,31)
160 xp160_0db0gy0ooy3gokaicz651230sw224oy1111wgy0oge2zggy0s03wgfy5a5az1qa17y0ddy1ccz023ycssszyc777 101 LCM(5,32)
165 xp165_y0dbzggci5ld3xog8oz0343zy275777757 45 LCM(11,15)
168 xp168_0g8gw3jzw1xqpwsszy211wc2w8k8zgggeeey066z333 44 LCM(8,21)
170 xp170_y6438g0ia4zx66w66xac4zxggo4c4oggyh66x66zca16888188861acya358mhh181hhm853zy066x66yj12321zyv66w66zym252x66 119 p5 shuttle
174 xp174_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cczzy9oiwm8gzyepg19 72 LCM(6,58)
175 xp175_ycca23zy746joozy033pc4zo8a6zxok4miewm9azxk4q11sjr8a6zy01 68 LCM(7,25)
176 xp176_y2ca23zws21q4zx11zxgc22szw8o121z311y125202vjq7zy72e841 59 LCM(16,22)
177 xp177_y3343x6bacy6cab6x343zkk8yy8kkzgo8gywg8ogz0123yw321zzgo4syws4ogzgh1yy1hgz221yy122zy3c2cx6d53y635d6xc2c 104 Karel
184 xp184_33y7cccd72ycssszccy7333be4y4ccy5777 40 LCM(8,46)
186 xp186_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy0ccb7w66zy166 64 LCM(6,31)
188 xp188_x696o8b9czy065x33xc871wbdzoozwgg04ahhha4y5c871z4701yfoozxggy0ggzx56w4701xmmggo5jzya146w343 108 capgun + boat-bit
189 xp189_y9g033zy6a9871zooyf789q8zy02bi2syf330oozybgs2iay24a4zy9oo01y96995a996zyvggw252zyv11 88 LCM(21,27)
190 xp190_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zy9i6vwv6izy911y011 62 LCM(5,38)
192 xp192_y1j3zy031d8ey6330gggg2u066zggy6s4c0gy0kg6w1z11y8hj1y1203vr2zya11 65 LCM(3,64)
196 xp196_yfccy28e1e88gzyeks8y2330311zyqoozwggzw11y6ggzg88c0ccy2132z0117871y233 66 H(pi)
200 xp200_32aczy0ooj64zy74cp33zyc6a8ozy2gggeeezy2333 42 LCM(8,25)
204 xp204_ybo8a6y1695qsozyigggy5g8k8ooozy1ggy7eehig421y31utzggwg9g89z14w61yfgzyi6511 79 LCM(4,102)
216 xp216_sssybg033zx777y5a9871zy1ooyf789q8zy52bi2syf33zyggs2iazyeoo01 68 LCM(8,27)
217 xp217_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy0a9mweim4kozy06a8rjs11q4kzy91 86 LCM(7,31)
225 xp225_y432aczy8ooj64zy5ggy44cp33z4s0gy0grqjy86a8ozwhhweh040hz4701y01rbpzy511 78 LCM(9,25)
226 xp226_y98oyn33y166z8oy732ys33y0ccz01219g8y2gkszwcq2qbyzy18e1eozx121yv8km8y27d11zxooyzy631e8zy3gg33ysdbzy311y133 107 nihonium*
228 xp228_yog8ka37acz32acyj37aczwsy1sy7sb4zy0222zyackgossssogkczy83552y42553 73 LCM(6,76)
230 xp230_033y133zzzckgsxsgkczzy4cczxggzojdwdjo 46 LCM(5,46)
231 xp231_8ehe8oy1o8a6zw12ll64y04a4zy056x66y1eh9mzyc3443wgw33zyh121 66 LCM(11,21)
232 xp232_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11z0gggeeez0333y4252y1252 66 LCM(8,29)
240 xp240_4r4y11h94c0ccz4r4y2fcw43 33 LCM(15,16)
246 xp246_ya32acydg8k8ooozyu1utzzzybcirrd6y4cc4zy1ggy61zggwg9g89z14w61ye354c 68 capgun
248 xp248_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zssszx777 60 LCM(8,31)
250 xp250_y1ooy2o4a9jwggzy1ccy0elh4wrwhhz33x6a2y134aipw11z252zzzzykggy94a4zygoowp452sgy6cczygoowtw2oa7y0jjzykc9521y211 119 p5 shuttle
252 xp252_8oymca23z0123ya4995zy9kii4yao8gzxo8a6ym32zyecc0v1e0u2c8a6zyh121e9156 78 LCM(9,84)
266 xp266_yeey0c871zya111cczyd4cgozgjjy1jjgz34daxad43z0ooy1ooy5ggzyd2301zya88833zye7y031e8 78 LCM(14,38)
275 xp275_y132aczy0ggxooj64z6246kh88y44cp33zcc0fip6sgnsy66a8ozy2346 71 LCM(11,25)
276 xp276_02hqzw37133zy9ei204oy766zy9sig086y7oozz6517x7156zzz0ooy1oo 62 LCM(3,92)
279 xp279_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy16a8850cs1v0cczy36519e121 84 LCM(9,31)
280 xp280_x352y364koz0ccx4r7y4gcgxoozy5ckggy033wgzgk2gb3y21y3123z11 56 LCM(8,35)
296 xp296_y632acy7oge2zwggy84bb6zx346yf62sgz0ccx66x6dd2z6om2y9354cz033 66 LCM(8,37)
297 xp297_y2o4cyag033z660u13grpd3y5a9871zc84c5h23wooyf789q8zy011y42bi2syf33zylgs2iazyjoo01 97 LCM(11,27)
304 xp304_gkkwptez330365sylca23zy94bsy7sy1szyp222zy6ckgossssogkczy43552y42553 78 LCM(16,76)
310 xp310_og8o0u1eoy5ooy3oozy0mlgrzx1qa2my2ov324sy3s423voz62460v0t6y13vo847y3748ov3zy21zye33y333 103 LCM(10,31)
312 xp312_yg33zy1g8gy6ieyag8gzy1121ym121zy2ogg8z33yq844cy033zzy1696yao4y6696zyi11zyg33 60 capgun + boat-bit
320 xp320_y13pmwmp3zy411y0cczcczx226wosr73wc88zyf66zy166 52 LCM(5,64)
325 xp325_0gs2ibaa4y5o8zlm0mlluy2sse321y3ca23z25s16a98gy846joozx11311y233pc4zy6o8a6 96 LCM(13,25)
336 xp336_x32acymo8zy979b4ya321z0g8oya4qisz23ym6a8ozx4ac0ca4z69ig4s0s4gi96zy01x1 76 LCM(16,84)
342 xp342_s0111zwi3y031e8zw1246zzzwg84czw9oy0oge2xggz70gggy46653w33zy269cey033zy5ci22ak8gzy94887 87 LCM(18,38)
360 xp360_9f9zbrby4a996z232y233y833zw66wd52666y666wba4666 59 LCM(15,72)
368 xp368_y2gy432aczy12251zzggyp62sgz56yc65134w16zyn4o68zy8o8go 48 capgun + boat-bit
380 xp380_ye3pmwmp3zcieg8oyb11z0suvy5sg2a4zg9jfgoz123zy7s0111zy9222x31e8 75 LCM(5,76)
385 xp385_xgbb88g0tb0gzca2t597432wh98cy34a6zx12y311y168c8xoozy033x1316y18ozy2652y3311 85 LCM(11,35)
392 xp392_y58cq7k8gzy8125sb62y5g8gzyf33y2qr0raa4zzyke2ex66zwccxe8ezz4aar0rby2oozx121 78 LCM(8,196)
408 xp408_y33bg2kgy5ckggzgggg8gy111y81z11101qt2y3259142sszy111y7111y7ig1jzyu12dw93zyb32ac 79 LCM(8,102)
418 xp418_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zygg88ggy24y1oge2zybo4cw332h1y1669b7zya11 82 LCM(22,38)
434 xp434_w33y333y5ccy1ccz86c8y38c68y2cmkgxgkmcz9fy7f9y6202z1631y31361y333y133zwccy3cc 82 LCM(14,31)
440 xp440_32acy866zx4q12sy7ggy0oq186zy111y561851zws22cgyh66zx121o8zy3113 62 LCM(22,40)
448 xp448_gjjy1jjgy266z34daxad43y9skh72w66z0ooy1ooy488ozy833w27411zym33 68 LCM(14,64)
455 xp455_ggy533y1ca230ggz0346yd643y0g0s4zy94rghey611zxo80ggzxg99gp6zx11y2ggy6eh1r4zy54701y0o4cydc4ozyc110o8a6y1ooy511 102 LCM(5,91)
460 xp460_033y133zzzckgsxsgkczzy979102cy733zy9e98043y7ccz31c08zy01050kgzy623 65 LCM(5,92)
465 xp465_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy3skssssks 60 LCM(15,31)
480 xp480_y5osq596z4r4y7oy0c871z4r4y6525zy366zy3gggeeezy3333 57 LCM(15,32)
496 xp496_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2oo0o8i22zy368wov 69 LCM(16,31)
512 xp512_yr33y166z0ggy033y16426ye33y0ccz011w66yuggz66yz56zzzy2mqyz66zygckgk2a21ya66woozy133y0ccye6426y1cczy566y1cc 100 capgun + boat-bit
552 xp552_x48r952wg8zsi4ogy113497zw21w8kir24zyjssszym777 48 LCM(8,138)
532 xp532_033y133zo4maxam4oylg88cz1ppy1pp1yggy01hzyf557y53088803zyaggy4ggzy8ckla26eeee62alkc 91 LCM(14,76)
550 xp550_32aczy0ooj64zy74cp33zw32acy66a8ozy14q12szy311zy0s22cgzy1121o8zy5113 66 LCM(22,25)
570 xp570_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zyfgcgzyfgfgzyg3 58 LCM(15,38)
594 xp594_yi330gzyk1789azy98q987yfooz64koy133yfs2ib2zx8k24oy7ai2sgzy01221ya10oozwo44ozw1242hgzy21226 92 LCM(22,27)
616 xp616_y066w3b8896zy9oieew66zzoggy1oozw23g8gy4oowccw4ozx16887y81111zxggzw78gb4zy26a8o 81 LCM(22,56)
651 xp651_w33y333yeg8oz86c8y38c68ybqb8oz9fy7f9y569e4y01226z1631y31361y18k8y6g8gzwccy3ccycggx1zyg32qkgow1343zyioge2 108 LCM(21,31)
682 xp682_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy7g88ggy24y1oge2zy2o4cw332h1y1669b7zy111 84 LCM(22,31)
690 xp690_0ooy9vtvzyc757zok4sxs4kozzzz033y133 40 LCM(15,46)
704 xp704_y2ca23zws21q4zx11zxgc22szw8o121y8ccz311wccy447zy977asszyas4y466zy666 72 LCM(22,64)
720 xp720_33y18kk8yb33zy8equyesksssskszy9757wggzccyb1221y1cc 54 LCM(15,144)
728 xp728_ggy533y1ca230ggz0346yd643y0g0s4zy94rghey611zzwgggeeezw333y2ggy6eh1r4zy54701y0o4cydc4ozyc110o8a6y1ooy511 96 LCM(8,91)
760 xp760_c88gyn33zw11ybgyas48g69gvz01110s0111y325dya3021zyaggy4ggyd33zy8ckla291hh192alkc 83 LCM(40,76)
770 xp770_y3352y364kozgy0ccx4r7y4gcgxooz1156y5ckggy033wgz08w7rp6y41y3123zzwcjrsw2zy2ckggzy51 80 LCM(22,35)
792 xp792_yf66w3b8896y666wcd1196zymccy4ggz4s0gy9gggyb66opo5zw1104ahiicy13448520o8gzyl32 83 LCM(22,72)
836 xp836_ydog8oy1o8ehe8zcieg8oye46ll21z0suvy5sg2a4y465zg9jfgoz123zy7s0111zy9222x31e8 90 LCM(11,76)
874 xp874_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zyacczzy9ca2exe2aczzzyaggy1ggzya11y111 72 LCM(38,46)
920 xp920_33zxs48g69gvzx3021yje9byb66zy833y3ooy3s4kyboozyr11 54 LCM(40,46)
924 xp924_8oymca23z0123ya4a75zy9ksa4yao8gzxo8a6ym32zykg88ggy24y1oge2zyfo4cw332h1y1669b7zye11 78 LCM(22,84)
960 xp960_x4evy2ve4zyacczcczx226wosr73wc88zyf66zy166 46 LCM(15,64)
966 xp966_033y133zo4maxam4oz1ppy1pp1y5gggzyg3047zy6sii6yagggzyn6443zydeigs 70 LCM(14,138)
988 xp988_yr33gzoggyi66w8653g80676211zw23ym4uezw70ggg07y44rry63zzy8o8bl46777764lb8ozy911y611 91 LCM(13,76)
992 xp992_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zyeggy2gggzwg8keey711xsss333zw1221y022525zy3o8a6 93 LCM(31,32)
1008 xp1008_0ooy1ooy033y18kk8yb33zwggxggydequze9d2x2d9eyc757wggz066y166y0ccyb1221y1cc 76 LCM(14,144)
1178 xp1178_ygsgh11zw66y366y533y031e8zgcogy3gocgy33356ziuy7uiz2c62y326c2zwooy3ooy5ookczyiooy0oge2zyg71hgg 92 LCM(31,38)"""

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
    return (pat, mpop, f"{n_gliders}G rectifier loop")

p4b1 = lt.pattern("""9bo$8bobo$9bo2$7b5o$o6bo3bo$2o7bo$2o6b3o$bo2b3o4bo$10b2o$2b2o$2b2o3bo$
3bo2bo$3b3o$2bo2bo6b3o$5bo$bo3b2o4bo2bo$2o10b2o$2o$o4$11bo$10bobo$10bo
bo$11bo$15b2o$15bobo$17bo$17b2o""")
p4b2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo4$18bo$17b2o$5b2o10b2o$4bo2bo4b2o3b
o$13bo$4b3o6bo2bo$13b3o$12bo2bo$11bo3b2o$15b2o$7b2o$7bo4b3o2bo$8b3o6b
2o$9bo7b2o$7bo3bo6bo$7b5o2$9bo$8bobo$9bo""")(17,32)

def p4_22hd_loop(p):
    if p%8 != 4 or p < 124:
        return None
    exts = (p-124) // 4
    return (p4b1 + p4b2(exts,exts), 136, "p4 22hd reflector loop")

mold = lt.pattern("3b3o$bob3o$obobo$o2bo$b2o")(-1,15)

def mold_rectifier_loop(p):
    if p%8 != 4 or p < 212:
        return None
    pat, mpop, source = rectifier_loop(p//2)
    return (pat+mold, mpop+12 if mpop != None else None, source + " + mold")

# 128+8n: p8 glider duplicator reflector with Coe's p8 and blocker
p8l1 = lt.pattern("""11b2o$11b2o3$11bo$9bobo$7bo2b2o$b2o5b2o$b2o5bo2$bo5b2o$obo4b2o$o2bo$bo
2bo5b2o$10b2o$bo2bo$b2o9$8bo$7bobo$7bobo$8bo$12b2o$12bobo$14bo$14b2o!""")
p8l2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo9$13b2o$13b2o$4b2o$4b2o7bo$12bobo$
7b2o3bo2bo$7b2o4bo2bo2$13bo2bo$7bo5b2o$5bobo$3bo2b2o$4b2o$4bo2$3b2o$3b2o!""")(14,34)
gp8l = lt.pattern("bo$2o$obo!")(9,16)
def p8_loop(p):
    if p%8 or p < 128:
        return None
    n_gliders, mpop = (2, 108) if p < 248 else (1, 103)
    exts = (p*n_gliders - 248) // 8
    pat = p8l1 + p8l2(exts,exts)[4*exts]
    for _ in range(n_gliders):
        pat = (pat+gp8l)[p]
    return (pat, mpop, f"{n_gliders}G p8 loop")

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
    return (pat, mpop, f"{n_gliders}G snark loop")

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
        res = (pd0_1 + pd0_2(exts,exts), 67)
    elif r == 1:
        res = (pd15_1 + pd15_2(exts,exts), 75)
    elif r == 2:
        res = (pd30_1 + pd30_2(exts,exts), 51)
    elif r == 3:
        res = (pd45_1 + pd45_2(exts,exts), 75)
    elif r == 4:
        res = (pd60_1 + pd60_2(exts,exts), 29)
    elif r == 5:
        res = (pd75_1 + pd75_2(exts,exts), 49)
    elif r == 6:
        res = (pd90_1 + pd90_2(exts,exts), 61)
    else:
        return None
    return res + (f"type-{r} pentadecathlon shuttle",)

# 90+24n: Elkies–Simkin 1hd reflector with p6 thumbs (p114 version is Ocellus)
p6ts1 = lt.pattern("""7b2o4bo$7b2o3bobo$13bo3$2o2b2o2b2o$2o2b2ob2o$9bo3$3b2o$2bo2b2o$2bo4b2o
$2o3bob2o$bobo$bob6o$2bo5bo$3b3o$5bo""")
p6ts2 = lt.pattern("""9bo$9b3o$6bo5bo$6b6obo$11bobo$6b2o2bo2b2o$6bobo2b2o$10bobo$11bo4$9b2o
2b2o$9b2o2b2o3$bo$obo3b2o$bo4b2o""")(13,3)

def p6thumb_shuttle(p):
    if p%24 != 18 or p < 90:
        return None
    return (p6ts1 + p6ts2((p-90)//8, (p-90)//8), 92, "p6 thumb shuttle")

# 66+6n: 22hd reflector with unices
# see https://conwaylife.com/forums/viewtopic.php?p=139947#p139947
p6l1 = lt.pattern("""9bo$4b2o3b3o$2obo8bo$2o2bo2bo3b2o$5bobo$6bo7b2o$14b2o$5b2o$5b2o9$12bo$
11bobo$11bobo$12bo$16b2o$16bobo$18bo$18b2o!""")
p6l2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo9$13b2o$13b2o$4b2o$4b2o7bo$12bobo$
7b2o3bo2bo2b2o$7bo8bob2o$8b3o3b2o$10bo!""")(20,28)
gp6l = lt.pattern("bo$2o$obo!")(13,8)

def p6_loop(p):
    if p%6 or p < 66:
        return None
    elif p%12 or p < 132:
        n_gliders, mpop = (4, 96)
    elif p%24 or p < 264:
        n_gliders, mpop = (2, 86)
    else:
        n_gliders, mpop = (1, 83)
    exts = (p*n_gliders - 264) // 8
    pat = p6l1 + p6l2(exts,exts)
    for _ in range(n_gliders):
        pat = (pat+gp6l)[p]
    return (pat, mpop, f"{n_gliders}G unix loop")

'''# 128+8n: p3 glider duplicator reflector
p3l1 = lt.pattern("""14bo$14b3o$17bo$16b2o2$19b2o$11b2o6b2o$4bo2bo3b2o$4bo2bo2b3o$bob2o2b2o
2bo$obo7b2o$bo3bo2bobo$5bo2bobo$5bo2b2o4$17bo$16bobo$16bobo$17bo$21b2o
$21bobo$23bo$23b2o!""")
p3l2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo4$15b2o2bo$14bobo2bo$14bobo2bo3bo$
13b2o7bobo$13bo2b2o2b2obo$12b3o2bo2bo$12b2o3bo2bo$4b2o6b2o$4b2o2$7b2o$
7bo$8b3o$10bo!""")(43,46)
gp3l = lt.pattern("bo$2o$obo!")(18,8)
def p3_loop(p):
    if p%3 or not p%6 or p < 51:
        return None
    n_gliders, mpop = (8, None)
    exts = (p*n_gliders - 408) // 8
    pat = p3l1 + p3l2(exts,exts)
    for _ in range(8):
        pat = (pat+gp3l)[p]
    return (pat, mpop, f"8G p3 loop")'''

# 98+56n: Elkies–Simkin 1hd reflector with 34P14 shuttles (p98 version is Gallus)
p14_1 = lt.pattern("""12b2o4bo$12b2o3bobo$18bo3$5b2o2b2o2b2o$5b2o2b2ob2o$14bo3$9bo$8b3o$2o4b
2o3bob2o$2o4bo2b2o2b2o$6bob2o4$6bob2o$2o4bo2b2o2b2o$2o4b2o3bob2o$8b3o$9bo""")
p14_2 = lt.pattern("""14bo$13b3o$5b2o4b2o3bob2o$5b2o4bo2b2o2b2o$11bob2o4$11bob2o$5b2o4bo2b2o
2b2o$5b2o4b2o3bob2o$13b3o$14bo4$9b2o2b2o$9b2o2b2o3$bo$obo3b2o$bo4b2o""")(19,0)

def p14_shuttle(p):
    if p%56 != 42 or p < 98:
        return None
    return (p14_1 + p14_2((p-98)//8, (p-98)//8), 105, "p14 shuttle")

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
        res = (tbs0_1 + tbs0_2(exts,exts), 60)
    elif r == 2:
        res = (tbs0_1 + tbs92_2(exts,exts), 77)
    elif r == 3:
        res = (tbs138_1 + tbs138_2(exts,exts), 72)
    else:
        return None
    return res + (f"type-{r} twin bees shuttle",)

cfuncs = (rectifier_loop, mold_rectifier_loop, p4_22hd_loop, p8_loop, snark_loop,
          pd_shuttle, p6thumb_shuttle, p6_loop, p14_shuttle, twinbees_shuttle)
