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
26 xp26_x32acz31e88g0653zy01pgz66w1023z66w8gkczy08pzc8711w6aczxc453 70 H(pi)
27 xp27_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910oo 56 56P27
28 xp28_033y133zo4maxam4oy1ggz1ppy1pp1xsta43 46 LCM(4,14)
29 xp29_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11zzy8252y1252 54 PPS
30 xp30_w33z8kqrqk8zzzw33 20 queen bee shuttle
31 xp31_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066 48 Merzenich
32 xp32_wosq596zy3oy0c871zy2525z66zgggeeez333 45 H(HF)
33 xp33_8ehe8oy1o8a6zw12ll64x88c04c6ezy056y313 46 LCM(3,11)
34 xp34_x4s0gy1ca23z4s0g011zw11y0ca2acy6oge2zgs26y6ckgkczyj31e8zy7ggkcy131e8zy71 74 H(pi)
35 xp35_y4ok46y3253zooxgcgy47r4xcczxgw33y0ggkczw321y31 44 H(HF)
36 xp36_32aczy08c8y0131zya354c 22 22P36
37 xp37_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354c 58 H(R)
38 xp38_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7 44 roc
39 xp39_xqh2z33173xccz4sk0emicy2oozy469dezy4327 46 LCM(3,13)
40 xp40_33zxs48g69gvzx3021zy833 26 Beluchenko
42 xp42_033y133zo4maxam4oz1ppy1pp1xgfnzyb1252333 50 LCM(6,14)
43 xp43_w2egoy03pm0eik8y18k8z4s0gzw11xcujy8pf6xggzyo1074zy2252y1259e0djoy031e8 80 capgun
44 xp44_0oql96xmqzgh1gxeqaa4oz1011y217871 45 LCM(4,11)
45 xp45_4ahhhhhha4zy94a6zx35c53zy166 29 H(pi)
46 xp46_033y133zzzckgsxsgkczz0cc 28 twin bees shuttle
47 xp47_w32acyeca23zy37y2ccy27z252xeaey8eaex252zg8gxsksy8sksxg8gz01y1oy2ccy2oy11zwggkc01ya10ckggzw1yk1 84 PPS
48 xp48_660259gcy1g8gzy166y1sspxgk2gb3zy8ooy011 44 LCM(6,16)
49 xp49_y466we91gzy5s2b0d43zy6897w66ybggzyh688c1lh6k0o99gzybn110kw66x1222x1zyb3ia9ozgx888gxccw50ggtz1ii305chlg622cz011ybccwsi2zyfo4m0q87zyf1giewcc 158 H(pi)
50 xp50_y132aczy5ooj64zwg08oy64cp33z320i9802i908oy46a8ozy33201 58 LCM(10,25)
51 xp51_g08o0u15gis89f0s48cz11wdbaik68jd0ddy1ca23zy232011y1sr7zy6o8a6y16a8o 90 LCM(3,17)
52 xp52_4s0gy3ca23zw11w4ed3zy08oy362sgzw311 35 H(LOM)
54 xp54_y566y2ca23z178cy14ksy6c871zxgozx31yadb 43 H(R)
55 xp55_y0dby06a8gzggci5ld3xogg150cgz0343y523y0346 49 LCM(5,11)
56 xp56_66625dw66zyb66zzy0oow8s26zy61ooo8kkwoozyc1 45 p56 B-heptomino shuttle
57 xp57_yzylg2tugzyzykof0cs7zyzyb8e96y21130186y0ggzyzyc117y8gg0643zyzw654y4o8a6y184sy211zzzyn361yd86czzy9gy6gzy1ooy2321y16511y42a6zgs26ybe88zy2618gc88gy16971zy4ujj0v1zy57b4 146 p3 22hd reflector loop
58 xp58_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cc 54 H(pi)
59 xp59_yg178cy0ca23zggz0346ybeahmm8zggkcy2gcc2ssy1111xgggz1y6323y7eehcd2y2ca23zyc4rr3ksybo8gzyf1yf32zy5ggkcy0c4ozy51y511 108 H(bun)
60 xp60_vtvy037bkicz757 24 LCM(4,15)
62 xp62_ccy069c536635c96y0cczz66y0ci6koccok6icy066zzy4ojd11djo 66 PS(5*12+2,31)
63 xp63_33j71t8ggz678u0h431zx223333zoo0u240s4ogkczx342sj2ac 70 LCM(7,9)
64 xp64_y1j3zy031d8ey633zggy6s4c0gz11y8hj1zya11 34 Merzenich
65 xp65_3pmwmp3zxh1gx21h2zx3c7a5301gk2w96zy5admlk 52 LCM(5,13)
66 xp66_y2ca23zws21q4zx11zxgc22szw8o121z311y0681hh4zy77 48 LCM(3,22)
68 xp68_gg032acy9ok46wggz0346yg643zyc221eeouizx8oyd2ll6o6426zy0123xsksy6101 71 H(pi)
69 xp69_y4gut2gzy47sc0fozggy06810311z0346xgg8ooy14aa4y3562zy51y76a8ozzykgoyfgkozyk101zzzyzw6a2ye163zzyzyl64kozyzyfgo8y38kk8y166522xo8gzyzyh1ydgw4oy032zyzyw6t1depzyzyx3geu3zyzyz1 146 p3 22hd reflector loop
70 xp70_033y133y1o62453zo4maxam4oy132156z1ppy1pp1 52 LCM(5,14)
71 xp71_y34s0gy439u0o4cz8oy311y5354t2acz0123y4cck88y111zx8oz0311yeca23zy688koozo80uigyd31e8z0phe0uby562sgzy1123 112 H(HF)
72 xp72_3bg2kgzy011y7ok46zy268ga4w8k24ozxo8a6 36 LCM(8,36)
74 xp74_y532acy5ca23zggyrggz0346y5636404636y5643zz0o4cy5coc404cocy5c4oz11yr11zy5o8a6y56a8o 84 Raucci
75 xp75_32acy9sksssskszy0ooj64zy74cp33zyc6a8o 42 LCM(15,25)
76 xp76_o4an7y1ca23yi32acz0110888xooxoa6ya6aoxoox888zy47ys7 56 LCM(4,38)
77 xp77_0jjg08c2a2oggcxqmz3w145431wccy3gozya8kkn9b4303213zyd1 67 LCM(7,11)
78 xp78_y45rc31zwmkac48g012640cczw1wgw1rozmkgino3s4z1w6221 61 LCM(6,13)
79 xp79_y232acydqmz4s0gywmqzgg11y5goy9re4y432acz1qa6y4136ykc4oz023y78oydggy211zya32yd1226 80 H(pi)
80 xp80_35426ox22i8o0ooz65123y1vow86 39 LCM(5,16)
81 xp81_yzyzwca23zyzyy33y2eu80gswsg0gzyzyw2a6y4178ewew121zyzyz0o4ozyzyugs26x1zyzyzxco4zyzyca64zzzyzyisg8zyu42ezzzyz08okzya86czyhoge2zyc696z0gxsws4oy5okgz1212ewe205vsy2ggzyaggkc011zya1 146 p3 22hd reflector loop
82 xp82_y3ggdby5ggozy2560797y3320g0s4z08ggy7ae4y011z112yh66wggozyn32zy8c4530ggzyd11y2go8y745a2zydgs26y111xg8g0ggzygc453y33ar452zys32 114 H(pi)
83 xp83_y22egoy3c871zyjc453z33y5442c4xgo0ggzy5ggoy51y733zy432y1g8oy3c4ozya23y711 62 H(R)
84 xp84_8oymca23z0123ya4995zy9kii4yao8gzxo8a6ym32 42 H(HF)
85 xp85_y2ccy6c871zzzy6a62y6os48a6zckg8ogyd3742aczok48f7y6gokzzzy4o4cy6cczy311 68 H(R)
86 xp86_y833y033z8oyoo8z0123y2757y2757y2321zzz0g8oy2sksy2sksy2o8gz23yo32zy8ooy0oo 76 H(TL)
87 xp87_ya32aczyfg8gw33y466zxg8gy81221zggw1oogyesscz11y2deeyd1266x33zycggy9252z0ooy4ggw3421zy711y2ckggzyi1 84 84P87
88 xp88_3bg2kgzy011y1o4oz3213xgonl9611zy5qm 45 LCM(8,11)
89 xp89_yzy833y58e1e88gzyzyj330311ybckzyzyd3224e6y725acy165lozyzwgs2552ypggzyzy2gcoy1o8a6xca8y911zzzzysgy1g0gzy4ooy9153x6511y113xggzggyx4aa43z1qa6y135a4y767244cz023yag88c0cczye117871y5cc 164 syringe-rectifier loop
90 xp90_gjjz1167w33y666zydca2aczyn256zyb75777757 45 LCM(6,45)
91 xp91_33j71t8ggz678u0h431zx223333xcczy04sk0emicy2oozy869dezy8327 68 LCM(7,13)
92 xp92_k0il96zghy8o4cybooz11y8hhhzy133y3346yb33 44 LCM(4,46)
93 xp93_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy44hh186zy57 60 LCM(3,31)
94 xp94_32acy1ca23zzy4ggy033z0ccx23423zyg66zzy066zybckic4x33zy6cczzy9c453y1354c 68 H(R)
95 xp95_gwg6t1e8gz11dlka211feow8gzy38o0122221zy41230oows48y12552y7g0gzyo354cy431zzzzyz46ayhgkozzzzzyzyk351yhac4zzzzyzyzy5goy464kozyzyzy5101y78kk8y1247w330o8gzyzyzyvg8888g032zyzyzyv12w3eugg8a5lmggzyzyzyzw12egnc1w1 166 p5 22hd reflector loop
96 xp96_0178cy766zy44koy6m640ooe4a4z0gs26x11xoy1oo022440ezo8go 59 capgun + boat-bit
97 xp97_ydg88e1u8y533z0kcyb11313kzol56y1ca52y6115137zy4ggyp2552sgzy411y94ocx6a8ozyzxe24zzzzyzy448ezyzyg32acx634y9ggzyzy4178kk8yp11zyzyksogkggy68ka6y1ckl3zyzyp5ogoggyb65zyzyeooy52fge221 164 syringe-rectifier loop
99 xp99_8oy3nl6z0123ws21913z8e13x12mmjy3mqzy53210gxeqaa4ozy66511y217871 82 LCM(9,11)
100 xp100_32aczy0ooj64zg88gy34cp33z125eey76a8o 42 LCM(4,25)
101 xp101_y364268e13zy9gy1oozy64671zxo4oy4562z255d0ddzyhggzooy533433y11074zycgzyb34b8oyf456zzywck4yf32q4ozyzyi1zyzya4s0gy1oo4ooy533zyzyc11zyzysmm0mkk8zyzyi8cky4343zyzylgsc4zyzye33y11zyzykoge2c84c 160 syringe-rectifier loop
102 xp102_ybc453zyeg8w4kk8y2gg8kbw9czy1ooy678c48by5408czooog8lb4zy01yeggozyi32 67 Raucci
103 xp103_yzyzyv33y58e1e88gzyzyzyzy3330311ybckzyzyzyz03224e6y725acy165lozyzyzylgs2552ypggzyzyzyxo8a6yf11zyzyzyma64y8742zzzzzyzyz4kcy86c2zzzzzyzy9gcoy8ca8zzzzzymg8oy88okzyo1ok46zy433ypg88ge2z6a8oy1ck8gy7os8gggy611z0bdy41y4g0ggy11zyd255t0t5y5ggzyh1y711 180 syringe-rectifier loop
104 xp104_gk2gb3y013cr5z11y0cc046210g84cakmzy8or1y11 46 LCM(8,13)
105 xp105_o08cbb2408fvy2skszff1024dd3101y2vnv 46 LCM(7,15)
106 xp106_y4696o8b9czy565x33y3szy04s0gy7222x222zy0gg11y12m2y1ggw6a8ozc88g0346y1121y11074zw1hosogy962sgzyeggzy9rb88ci9gzya23w121 115 H(TB)
108 xp108_y432acy266zx178cy6sk4y1c871zciakgyfogzw133xbdya13 55 LCM(4,54)
110 xp110_c4oy1178cwggg2y2oo4kozx160kgy235433y28111w62sgzy412ac 51 LCM(5,22)
111 xp111_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z47010ggo08ocsg0354czy38kcc6249szy832q5k46zyb11 97 LCM(3,37)
112 xp112_om999e0e999mozx8kc0ck8zzw8if505fi8 50 LCM(14,16)
113 xp113_ggy666y0c871z0346zy8gggy7cczy83wbow330oowoozzy9ggwggy1gzy911w110ccw1dggszy933zyx62sgzyf8e13y066 86 capgun
114 xp114_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zye4hh186zyf7 57 LCM(3,38)
116 xp116_y6o4an7zy711zy166y5ok4kozym31e8zx32acyc6a8oz2egozy535453y5cc 68 LCM(4,58)
117 xp117_x32acxca23zggxg84448gxggy2g88cz14fes72x27sef41y211zyfeehrzyq33zyfo8gy5g33zyfopw11267608g3568w66zyseu4zyu3 112 LCM(9,39)
120 xp120_4r4y13bg2kgz4r4y511 24 LCM(8,15)
124 xp124_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy337bkic 60 LCM(4,31)
126 xp126_0ccy1ccx32acxca23zcmkgxgkmcy24r4zy0202y64r4z033y133xo8a6x6a8o 74 LCM(9,14)
127 xp127_y932aczy366y4sccy44a4zyd44c5ko8zyh1ya33zccy9gozya112a32izy3252y4333y466zyh354c 74 H(C)
128 xp128_xo444kgwooy42560652zxc98g11y53diiie0eiiid3zy111zy66a8a6zc453yd354czy6444 80 H(pi)
129 xp129_ggyhca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyyc453 38 H(R)
130 xp130_x32acz31e88g0653zy01pgz66w1023y3o8gkcz66w8gkcy23c84kozy08pzc8711w6aczxc453 88 LCM(5,26)
132 xp132_252w253zy0gxggg0ooozy13w3488a61oml1hiswcgzw695qsoy3111zyica4w4a4 72 LCM(4,33)
135 xp135_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910ooy2uquzyjfbf 68 LCM(15,27)
138 xp138_w8gw259r84z79431y1go4iszx42rik8w12 36 Gabriel
140 xp140_033y133zo4maxam4oy1gy1gs26z1ppy1pp1y0121ggcaaq552zy8ok46o7o7421zyd1 82 LCM(14,20)
141 xp141_y64a4y14a4w178cx8e1e8gzy2sy0cscxcscy0sx33159d11z8e13yj31e8z8oy133y933y1o8z0123wsy0osoxosoy0sw321zy6g8gy1g8gzy71y31 114 PS(7*20+1,47)
143 xp143_0gs2ibaa4y5o8zlm0mlluy2sse321wbdz25s16a98gxo8gox13tlicggzx11311yb343 99 LCM(11,13)
144 xp144_33y18kk8yb33zy8equzy9757wggzccyb1221y1cc 42 Achim
146 xp146_4s0gyica23zw11y2ei0iezwo8a6y21zy466w4acxsexes 52 H(pi)
148 xp148_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701x888gy0354czxca2ro8g2i0sz031132y11 89 LCM(4,37)
150 xp150_w178cxg8zy417gukzy75f1sgzccb7w66y121x62sgz066 46 LCM(6,25)
152 xp152_32acywca23zwsy48kie4y84eik8y4szy1771yo177zybgggeeezyb333 60 LCM(8,38)
154 xp154_gjjy1jjgz34daxad43z0ooy1ooy2ok4ooy22gggwc871zy6gs26w1118y233453 70 LCM(14,22)
154 xp154_o08cbb2408fvzff1024dd3101y1ok4ooy22gggwc871zy7gs26w1118y233453 70 LCM(7,22)
155 xp155_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2idiidizy31w1 64 LCM(5,31)
160 xp160_y42egoy533z0oggzx23ye8sky3cczz66y3572yeo8zyr113zy8ooy531e8 56 H(pi)
164 xp164_y5ggdby5ggozy4560797y3320g0s4zx8ggy7ae4y011z0gh12yh66wggoz34a9gayj32zyac4530ggzyf11y2go8y745a2zyfgs26y111xg8g0ggzyic453y33ar452zyu32 126 LCM(4,82)
165 xp165_y0dbzggci5ld3xog8oz0343zy275777757 45 LCM(11,15)
166 xp166_y031e8zwo8b513z0ggo0ooy444sy4ooz122ege2y123011zypo4ozy3ccy4sii031y1dd0d552zypg88czynbq23zyo123 102 H(R)
168 xp168_0g8gw3jzw1xqpwsszy211wc2w8k8zgggeeey066z333 44 LCM(8,21)
170 xp170_y6438g0ia4zx66w66xac4zxggo4c4oggyh66x66zca16888188861acya358mhh181hhm853zy066x66yj12321zyv66w66zym252x66 119 p5 shuttle
172 xp172_y833y033z8oyoo8z0123y2757y2757y2321zzz0g8oy2sksy2sksy2o8gz23yo32zy8ooy0ooy4k0il96zyp1 88 LCM(4,86)
174 xp174_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cczzy9oiwm8gzyepg19 72 LCM(6,58)
175 xp175_32aczy0ooj64zy74cp33zyc6a8ozy3mf0g066zy235t0bqczy166xf6 64 LCM(7,25)
176 xp176_y2ca23zws21q4zx11zxgc22szw8o121z311y125202vjq7zy72e841 59 LCM(16,22)
177 xp177_y3343x6bacy6cab6x343zkk8yy8kkzgo8gywg8ogz0123yw321zzgo4syws4ogzgh1yy1hgz221yy122zy3c2cx6d53y635d6xc2c 104 Karel
184 xp184_33y7cccd72ycssszccy7333be4y4ccy5777 40 LCM(8,46)
185 xp185_ya3pmwmp3zy432acy111y0oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354c 76 LCM(5,37)
186 xp186_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy0ccb7w66zy166 64 LCM(6,31)
187 xp187_ygoggydca23zyi23zyb4s0gy63d8ezyd11yj62sgzzy6o4ozy3255d0ddzysbr0raa4zyt121zggz0346yjo8gzy971bcy832zyickggzwc453yf1 112 H(C)
188 xp188_y032acy1ca23zzy8ggy033zy1ccx23423zyk66zzy466zo4k8ybckic4x33z01277y5cczzydc453y1354c 80 LCM(4,94)
189 xp189_y9g033zy6a9871zooyf789q8zy02bi2syf330oozybgs2iay24a4zy9oo01y96995a996zyvggw252zyv11 88 LCM(21,27)
190 xp190_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zy9i6vwv6izy911y011 62 LCM(5,38)
192 xp192_y1j3zy031d8ey6330gggg2u066zggy6s4c0gy0kg6w1z11y8hj1y1203vr2zya11 65 LCM(3,64)
196 xp196_yfccy28e1e88gzyeks8y2330311zyqoozwggzw11y6ggzg88c0ccy2132z0117871y233 66 H(pi)
199 xp199_yc33y366y333zccyzy5cczye6kkgy4gkk6zy4ggysggzy4hhyshhzy411ys11zyec551y4155cz66yzy566zycooy3ccy3oo 84 H(LOM)
200 xp200_32aczy0ooj64zy74cp33zyc6a8ozy2gggeeezy2333 42 LCM(8,25)
204 xp204_ybo8a6y1695qsozyigggy5g8k8ooozy1ggy7eehig421y31utzggwg9g89z14w61yfgzyi6511 79 LCM(4,102)
210 xp210_033y133y3gcgzo4maxam4oy2gfgz1ppy1pp1y33 46 LCM(14,15)
215 xp215_g8gg8gx8k8y18kie0mp3y0oge2z4b44b4ylg0s4zy1ggx1ppy8jjgx11zx4701zy18e13y0ojd0e952y1252 96 LCM(5,43)
216 xp216_y332acy266zw178cy6sk4y1c871z0ccygogz6om2yf13z033 52 LCM(8,54)
217 xp217_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2660g0fmzy3cqb0t53zy46fx66 82 LCM(7,31)
220 xp220_ya32acy06a4zysoge2zo8goy04aicy5771332y5cik8y06246zy8gs26zyj8koy0ckggzyt1 74 H(HF)
222 xp222_2egoy7ca23zy56bb4y8ggzgs26yf643zya2dd6x66xcczy4c453y966qswcc 67 LCM(6,37)
225 xp225_y432aczy8ooj64zy5ggy44cp33z4s0gy0grqjy86a8ozwhhweh040hz4701y01rbpzy511 78 LCM(9,25)
226 xp226_y032aczz0ccy7s44y8ooy0oozybhh032y5ccycbdzcky9110ccy5gg033z11y666y066y61099ey7cczzyzwckggzyzy11 86 capgun + boat-bit
228 xp228_yog8ka37acz32acyj37aczwsy1sy7sb4zy0222zyackgossssogkczy83552y42553 73 LCM(6,76)
230 xp230_033y133zzzckgsxsgkczzy4cczxggzojdwdjo 46 LCM(5,46)
231 xp231_8ehe8oy1o8a6zw12ll64y04a4zy056x66y1eh9mzyc3443wgw33zyh121 66 LCM(11,21)
232 xp232_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11z0gggeeez0333y4252y1252 66 LCM(8,29)
232 xp232_y53bg2kgzy911zzy5ok4koy566z8e13zxo8a6ycca23zymoge2zy1ccy535453 66 LCM(8,58)
235 xp235_3pmwmp3x8k8y18k8y4ggzx110gggybggg0643z0gs26y3cecxceczy466y966zy2gggx373x373xgggz0gs26y3gy3gy362sgzy7121y1121 102 LCM(5,47)
236 xp236_yg178cy0ca23zggz0346ybeahmm8zggkcy2gcc2ssy1111xgggz1y6323y7eehcd2y2ca23zxo4k8y54rr3ksybo8gzy01277y71yf32zy5ggkcy0c4ozy51y511 120 LCM(4,59)
240 xp240_4r4y11h94c0ccz4r4y2fcw43 33 LCM(15,16)
246 xp246_ya32acydg8k8ooozyu1utzzzybcirrd6y4cc4zy1ggy61zggwg9g89z14w61ye354c 68 capgun
248 xp248_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zssszx777 60 LCM(8,31)
250 xp250_y1ooy2o4a9jwggzy1ccy0elh4wrwhhz33x6a2y134aipw11z252zzzzykggy94a4zygoowp452sgy6cczygoowtw2oa7y0jjzykc9521y211 119 p5 shuttle
252 xp252_vf8042bbc80oz1013dd4201ffyaca23zyc131y08c8zy8c453 56 LCM(7,36)
258 xp258_xggyhca23zy0346ycggzyi13zcg952066yygs8z066yzyi62sgzyzwc453 54 LCM(6,129)
259 xp259_ckgoxc871zcimikswccy0g88czxmqy066x11zy4aiicy7c871zy0o4cy7ciikzx11zy8c453y2354c 87 LCM(7,37)
260 xp260_x32acz31e88g06530ggwg8gzy01pggx12269ahu248gz66y0231y1ckow3dhlaa4z66xgks8y9346zy08pzc8711w6aczxc453 118 LCM(20,26)
266 xp266_yeey0c871zya111cczyd4cgozgjjy1jjgz34daxad43z0ooy1ooy5ggzyd2301zya88833zye7y031e8 78 LCM(14,38)
266 xp266_33j71t8ggz678u0h431zx223333wssgyogsszy47y4259e4y84e952y47zy2o8a6yw6a8o 78 LCM(7,38)
273 xp273_yjmf0g066zy4o4cy735t0bqczx321f811y766xf6zyio8gwooz6246y2636y61oggzyaggy3sd4pzya11x66x110ciqs0ae8zylcc 111 LCM(7,39)
275 xp275_y132aczy0ggxooj64z6246kh88y44cp33zcc0fip6sgnsy66a8ozy2346 71 LCM(11,25)
276 xp276_02hqzw37133zy9ei204oy766zy9sig086y7oozz6517x7156zzz0ooy1oo 62 LCM(3,92)
279 xp279_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy16a8850cs1v0cczy36519e121 84 LCM(9,31)
280 xp280_x352y364koz0ccx4r7y4gcgxoozy5ckggy033wgzgk2gb3y21y3123z11 56 LCM(8,35)
282 xp282_32acy1ca23zzy4ggy033y4ggo08ocsz0ccx23423yb26zyg66zzy066zybckic4x33zy6cczzy9c453y1354c 80 LCM(3,94)
292 xp292_0g40k8w7exe7x6a4wccz34521ybgy2ca23zyee909ey2ggzxo8a6yi1074 64 LCM(4,146)
295 xp295_yg178cy0ca23zggz0346ybeahmm8zggkcy2gcc2ssy1111xgggz1y6323y7eehcd2y2ca23zwg8gg8gy44rr3ksybo8gzw4b44b4y71yf32zy5ggkcy0c4ozy51y511 124 LCM(5,59)
296 xp296_y632acy7oge2zwggy84bb6zx346yf62sgz0ccx66x6dd2z6om2y9354cz033 66 LCM(8,37)
297 xp297_y2o4cyag033z660u13grpd3y5a9871zc84c5h23wooyf789q8zy011y42bi2syf33zylgs2iazyjoo01 97 LCM(11,27)
301 xp301_w2egoy03pm0eik8y18k8x8ggo8jacs0grjz4s0gymcdw335c11w1zw11xcujy8pf6xggzyo1074zy2252y1259e0djoy031e8 114 LCM(7,43)
304 xp304_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zyc25202vjq7zyf2e841 65 LCM(16,38)
310 xp310_og8o0u1eoy5ooy3oozy0mlgrzx1qa2my2ov324sy3s423voz62460v0t6y13vo847y3748ov3zy21zye33y333 103 LCM(10,31)
312 xp312_yg33zy1g8gy6ieyag8gzy1121ym121zy2ogg8z33yq844cy033zzy1696yao4y6696zyi11zyg33 60 capgun + boat-bit
320 xp320_y13pmwmp3zy411y0cczcczx226wosr73wc88zyf66zy166 52 LCM(5,64)
322 xp322_033y133zo4maxam4oy1ooy1ooz1ppy1pp1zzzyb3547x7453zzyj33 62 LCM(14,46)
322 xp322_660g0fmz0cqb0t53zw6fx66zy2ooybc4ozyjhhhzy233yb643y333 62 LCM(7,46)
325 xp325_0gs2ibaa4y5o8zlm0mlluy2sse321y3ca23z25s16a98gy846joozx11311y233pc4zy6o8a6 96 LCM(13,25)
330 xp330_178cwggg2y2oo4kozy235433y28111w62sgzz4evy2ve4 48 LCM(15,22)
333 xp333_2egoy7ca23zy56bb4y8ggzgs26yf643wg88gzya2dd6x66x62adhhzy4c453y66a88bbahe21zyj33w32 94 LCM(9,37)
336 xp336_8oymca23z0123ya4b97zy9siq4yao8gzxo8a6ym32zyd4a404u6kezyg4sh93 65 LCM(16,84)
342 xp342_s0111zwi3y031e8zw1246zzzwg84czw9oy0oge2xggz70gggy46653w33zy269cey033zy5ci22ak8gzy94887 87 LCM(18,38)
344 xp344_gk2gb3y5ccy0ccz11zx178cy2sksy2sksy2c871zzzy9gggy2gggzx8e13y2323y2323y231e8zzyb33y033 88 LCM(8,86)
351 xp351_y9g033zy6a9871zooyf789q8zy02bi2syf33xcczybgs2iay14sk0emicy2oozy9oo01yc69dezyt327 90 LCM(13,27)
360 xp360_y94evy2ve4zyn4a6zyc27dod72zxsssy877z777 41 LCM(8,45)
368 xp368_y2gy432aczy12251zzggyp62sgz56yc65134w16zyn4o68zy8o8go 48 capgun + boat-bit
370 xp370_2egoy7ca23zy56bb4y8ggzgs26yf643y04ka8zya2dd6x66xccc4ak8g086o4zy4c453y44ka8w6acwefzyl86o4 97 LCM(10,37)
376 xp376_yf32acy1ca23zggz1581qoy633y0ggzyh1663y0cczy666zzym66zy333y0cmm8zygcczzy2c453y1354c 82 LCM(8,94)
378 xp378_yd32acy266zy8178cy6sk4y1c871zgx888gxccygogz1ii305chlg622cyf13z011 71 LCM(7,54)
380 xp380_ye3pmwmp3zcieg8oyb11z0suvy5sg2a4zg9jfgoz123zy7s0111zy9222x31e8 75 LCM(5,76)
381 xp381_xguydca23z618882w4a4y1oocmey566zyc8sc0326z033zyigyacczyd64cg3jhzy466y576311y1252zyac453 86 LCM(3,127)
385 xp385_xgbb88g0tb0gzca2t597432wh98cy34a6zx12y311y168c8xoozy033x1316y18ozy2652y3311 85 LCM(11,35)
387 xp387_y3o487p8a6zggw330f860743156y2ca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyyc453 74 LCM(9,129)
392 xp392_y58cq7k8gzy8125sb62y5g8gzyf33y2qr0raa4zzyke2ex66zwccxe8ezz4aar0rby2oozx121 78 LCM(8,196)
407 xp407_yc32acy7oge2zy4ggy84bb6zgg0g4cx346yf62sgz101p542mgx66x6dd2z330347o6l56y8354czy311 92 LCM(11,37)
408 xp408_y33bg2kgy5ckggzgggg8gy111y81z11101qt2y3259142sszy111y7111y7ig1jzyu12dw93zyb32ac 79 LCM(8,102)
414 xp414_w6a897o4oz6511a0338f033zy0ooybc4ozyhhhhzy033yb643y333 64 LCM(9,46)
415 xp415_ye178cy3oge2zy8354czxg8gy5gg0ogx4c244y54a4zxghy81y5oggzojdwdjoxo4cy3o8gy123zy611y732 80 LCM(5,83)
418 xp418_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zygg88ggy24y1oge2zybo4cw332h1y1669b7zya11 82 LCM(22,38)
423 xp423_8oy3nl6z0123ws21913y6gy3gz8e13x12mmjy5121y1121y2oge2zy5321g8ow7y0373x373y07zy723y1ooy9oozzy8g8ow7y0676x676y07wo8gzy723y44a4y14a4y432 132 LCM(9,47)
424 xp424_y03bg2kgzy411zggx66y366z0346y1888z2egoy14l4y162sgzydo8gzy1ooy3oox32zzy7777ooozya111 80 LCM(8,106)
430 xp430_idiidiy5ccy0ccz01w1zx178cy2sksy2sksy2c871zzzy9gggy2gggzx8e13y2323y2323y231e8zzyb33y033 92 LCM(5,86)
432 xp432_xogyamqxdv9ae2gkozx13yf4a4x1zgs26y1457y662sgzy5ccy26a8o 64 LCM(16,54)
434 xp434_w33y333y5ccy1ccz86c8y38c68y2cmkgxgkmcz9fy7f9y6202z1631y31361y333y133zwccy3cc 82 LCM(14,31)
438 xp438_y4oow8kcxesxsexcg952066zw64koyj66zy6si1isz8e13yickggzyp1 68 LCM(6,146)
440 xp440_32acy866zx4q12sy7ggy0oq186zy111y561851zws22cgyh66zx121o8zy3113 62 LCM(22,40)
448 xp448_gjjy1jjgy266z34daxad43y9skh72w66z0ooy1ooy488ozy833w27411zym33 68 LCM(14,64)
455 xp455_ggy533y1ca230ggz0346yd643y0g0s4zy94rghey611zxo80ggzxg99gp6zx11y2ggy6eh1r4zy54701y0o4cydc4ozyc110o8a6y1ooy511 102 LCM(5,91)
460 xp460_033y133zzzckgsxsgkczzy979102cy733zy9e98043y7ccz31c08zy01050kgzy623 65 LCM(5,92)
465 xp465_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy3skssssks 60 LCM(15,31)
470 xp470_32acy1ca23zzy4ggy033y5idiidiz0ccx23423yb1w1zyg66zzy066zybckic4x33zy6cczzy9c453y1354c 84 LCM(5,94)
480 xp480_y5osq596z4r4y7oy0c871z4r4y6525zy366zy3gggeeezy3333 57 LCM(15,32)
481 xp481_2egoy7ca23zy56bb4y8ggzgs26yf643zya2dd6x66wcczy4c453y3ooy2cime0ks4zyjed96zyk723 85 LCM(13,37)
494 xp494_y1gy432acywca23zg8e1pl552y2888xooxoa6ya6aoxoox888zar0raavy2eesgg07ys7z12egjlkk8y31074zy11 110 LCM(13,38)
496 xp496_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2oo0o8i22zy368wov 69 LCM(16,31)
506 xp506_32acz0gwemicy366zy111zwo6mow4y16517x7156zx111o8zy3113zybooy1oo 66 LCM(22,46)
508 xp508_y2osq596xoozzy2252yi33zy8gcogyfoge2zwggxee810f2y5gg4v08177z4701yg13zy2ccyi4a4zyiggzyi11 86 LCM(4,127)
516 xp516_ggyhca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyp37bkicxc453 50 LCM(4,129)
518 xp518_2egoy7ca23zy56bb4y8ggzgs26yf6430ooy1oozya2dd6x66y3808zy4c453ya6d51x15d6zyn66y166 85 LCM(14,37)
528 xp528_252y2gy9cgwgz652y2o99gy61e6rargzy4stgc87y57zy6s261n7zy71ii3y28kczya1y28k8 81 LCM(16,33)
528 xp528_0qr10330jmz06c0cc08d5y1178cwggg2y2oo4kozy9o88y135433y28111w62sgzxgggy311zsss333 81 LCM(22,48)
530 xp530_y13pmwmp3zy411z8ox33y333z0123y14c4z178cy1252y131e8zydc4ozy1ccy3ccx11zy2gg88ggzy1c96w69c 88 LCM(5,106)
552 xp552_x48r952wg8zsi4ogy113497zw21w8kir24zyjssszym777 48 LCM(8,138)
532 xp532_033y133zo4maxam4oylg88cz1ppy1pp1yggy01hzyf557y53088803zyaggy4ggzy8ckla26eeee62alkc 91 LCM(14,76)
550 xp550_32aczy0ooj64zy74cp33zw32acy66a8ozy14q12szy311zy0s22cgzy1121o8zy5113 66 LCM(22,25)
560 xp560_y4ok46y3253zooxgcgy47r4xcczxgw33y0ggkczw321y3108k84a1a4w66zyfssszyc777 72 LCM(16,35)
570 xp570_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zyfgcgzyfgfgzyg3 58 LCM(15,38)
584 xp584_y14s0gy1ca23zwoox11z0ok8y14ahhrycsssz8oogyj777zgoo8zyc62sg 65 LCM(8,146)
592 xp592_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354czx33x77304a4zy36m048zy51033 86 LCM(16,37)
594 xp594_ya32acy266z64koy1178cy6sk4y1c871zx8k24oyiogzy01221yi13zwo44ozw1242hgzy21226 73 LCM(22,54)
597 xp597_yc33y366y333zccyzy5cczye6kkgy4gkk6ye44mg2637zy4ggysggy71zy4hhyshhzy411ys11zyec551y4155cz66yzy566zycooy3ccy3oo 96 LCM(3,199)
616 xp616_y066w3b8896zy9oieew66zzoggy1oozw23g8gy4oowccw4ozx16887y81111zxggzw78gb4zy26a8o 81 LCM(22,56)
635 xp635_y2g0k413y6ok46zwo0a0208k8y1ggocsy5ccz32yahpo164cz066ya1zyxoozydc8o0672zy4ccy5ed633y14a4zyao8a6 89 LCM(5,127)
638 xp638_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cczygggozycg8g32zyb78861zyeggzyc4bg87zy9o8a6 92 LCM(22,58)
645 xp645_y232aczz4r4z4r4y5gzxg8oy1311zw23zzypo8zyfggoy1321zyg1zzzyj6a8o 50 LCM(15,129)
651 xp651_w33y333yeg8oz86c8y38c68ybqb8oz9fy7f9y569e4y01226z1631y31361y18k8y6g8gzwccy3ccycggx1zyg32qkgow1343zyioge2 108 LCM(21,31)
664 xp664_ye178cy3oge2zy8354czybgg0ogx4c244y533zy033y71y5oggzxsssy1o4cy3o8gy123z777y311y732 74 LCM(8,83)
682 xp682_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy7g88ggy24y1oge2zy2o4cw332h1y1669b7zy111 84 LCM(22,31)
690 xp690_0ooy9vtvzyc757zok4sxs4kozzzz033y133 40 LCM(15,46)
704 xp704_y2ca23zws21q4zx11zxgc22szw8o121y8ccz311wccy447zy977asszyas4y466zy666 72 LCM(22,64)
720 xp720_33y18kk8yb33zy8equyesksssskszy9757wggzccyb1221y1cc 54 LCM(15,144)
730 xp730_4q44q4x7exe7x6a4wccz121121ybgy2ca23zyfe909ey2ggzy0o8a6yi1074 68 LCM(5,146)
760 xp760_c88gyn33zw11ybgyas48g69gvz01110s0111y325dya3021zyaggy4ggyd33zy8ckla291hh192alkc 83 LCM(40,76)
762 xp762_066yica23z33dew66x4a4y1oocmey566zyf8sc0326zy033zylgyacczyg64cg3jhzy766y576311y1252zydc453 90 LCM(6,127)
770 xp770_y3352y364kozgy0ccx4r7y4gcgxooz1156y5ckggy033wgz08w7rp6y41y3123zzwcjrsw2zy2ckggzy51 80 LCM(22,35)
792 xp792_yf66w3b8896y666wcd1196zymccy4ggz4s0gy9gggyb66opo5zw1104ahiicy13448520o8gzyl32 83 LCM(22,72)
796 xp796_y333yn33zyfooxoozz66y5os8gybg8soy566zy913yb31z033yz33zggy5csa7yb7ascy5ggz11yzw11zyfccxcczzy333xosq596ye33 96 LCM(4,199)
828 xp828_033y133zzzckgsxsgkczzy4ccyaca23zya131y08c8zy6c453 50 LCM(36,46)
836 xp836_ydog8oy1o8ehe8zcieg8oye46ll21z0suvy5sg2a4y465zg9jfgoz123zy7s0111zy9222x31e8 90 LCM(11,76)
874 xp874_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zyacczzy9ca2exe2aczzzyaggy1ggzya11y111 72 LCM(38,46)
889 xp889_xo4k6k9b88gz259am2230311w64kozwbdy0ccy4oooy48k8zye98oa8ggzyi31y966z0ooyagzyb235k644zy44a4y4667y4cczyi6a8o 115 LCM(7,127)
903 xp903_ggyhca23z0346ycggzyf13zyzy0gs8zyzyi62sgzynmf0g066y0c453zym35t0bqczyl66xf6 72 LCM(7,129)
920 xp920_33zxs48g69gvzx3021yje9byb66zy833y3ooy3s4kyboozyr11 54 LCM(40,46)
924 xp924_8oymca23z0123ya4a75zy9ksa4yao8gzxo8a6ym32zykg88ggy24y1oge2zyfo4cw332h1y1669b7zye11 78 LCM(22,84)
960 xp960_x4evy2ve4zyacczcczx226wosr73wc88zyf66zy166 46 LCM(15,64)
966 xp966_660g0fmz0cqb0t53zw6fx66zyd8gw259r84zyb79431y1go4iszye42rik8w12 70 LCM(7,138)
988 xp988_yr33gzoggyi66w8653g80676211zw23ym4uezw70ggg07y44rry63zzy8o8bl46777764lb8ozy911y611 91 LCM(13,76)
995 xp995_y333yn33zyfooxoozz66y5os8gybg8soy566zy913yb31z033yz33zggy5csa7yb7ascy5ggz11yzw11zyfccxcczzy333xgc26yg33zy3g8a03zy0651 99 LCM(5,199)
1008 xp1008_0ooy1ooy033y18kk8yb33zwggxggydequze9d2x2d9eyc757wggz066y166y0ccyb1221y1cc 76 LCM(14,144)
1016 xp1016_ggykca23z1581qoy24a4y1oocmey566zyg8sc0326zy133zymgyacczyh64cg3jhzy866y576311y1252zyec453 86 LCM(8,127)
1022 xp1022_y4ccw4a6x7exe7zw32acy2gzwggy2e909ez4701yi6a8ozzyaccxuczybokn0qb6zycdu010cc 86 LCM(7,146)
1032 xp1032_yy32acyhggzyzy0ggyc643zyzy131zyf8sgzgs26zy9sssy3354czy6777 50 LCM(8,129)
1104 xp1104_w8gw259r84ybu6w4oz79431y1go4isy7ghi46066zx42rik8w12 57 LCM(16,138)
1150 xp1150_y232aczy6ooj64z0ggy1ggy34cp33z011y111y86a8ozzz6a8exe8a6zzy466 58 LCM(25,46)
1178 xp1178_ygsgh11zw66y366y533y031e8zgcogy3gocgy33356ziuy7uiz2c62y326c2zwooy3ooy5ookczyiooy0oge2zyg71hgg 92 LCM(31,38)
1330 xp1330_y433y08kczwg8ox27b4z023y5g0s4z0gx2de4x110ssgyogssz321y0ccx7y4259e4y84e952y47zy6o8a6yw6a8o 88 LCM(35,38)
1480 xp1480_yd2vssy233zyggggzy8ccy233f4zy432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354c 84 LCM(37,40)
1518 xp1518_y2ca23zws21q4zx11zxgc22szw8o121y9si2ez311yno88gzy9eiioya223zyjg08ozyj3221 72 LCM(22,138)
1584 xp1584_oggy633y18kk8yb33zw23gggyeequz04w3dc3ye757wggzxggy4ccyb1221y1cczw69dew1zy26a8o 78 LCM(22,144)
1606 xp1606_64koy332acyig0s4zx8k24oyeei0iey211zy01221yg1y26a8ozwo44oy6sexesxca4w66zw1242hgzy21226 88 LCM(22,146)
1900 xp1900_yb32aczyfooj64zg8oyj4cp33z1a16p3yl6a8oz380gfy226862z69e123zyaezy61110sy0c4ozyh11 87 LCM(25,76)
1905 xp1905_y932aczy366y4sccy44a4zyd44c5ko8zyh1ya33zccy9gozya112a32iz0gcgx252y4333y466z0gfgyd354czw3 86 LCM(15,127)
1932 xp1932_8oymca23z0123ya4a75zy9ksa4yao8gzxo8a6ym32zy8oozzy7ok4sxs4kozzzzy833y133 72 LCM(46,84)
2156 xp2156_yfccy28e1e88gzyekksy2330311zyqoozwggyrgggy9g0s4zw11y5gggy9g8o0258443y1ciiha4011zg88c0ccy2322y823z0117871y233 104 LCM(22,196)
2356 xp2356_w33y333z86c8y38c68ynca23z9fy7f9y44bsy7sy1sz1631y31361yk222zwccy3ccy3ckgossssogkczye3552y42553 105 LCM(31,76)
2920 xp2920_y4ccw4a6x7exe7zw32acy2gzwggy2e909ez4701yi6a8ozzy7oozye6aiiazyca99aczym33 78 LCM(40,146)
2794 xp2794_y932acya178cwggg2y2oo4kozy366y4sccy44a4y235433y28111w62sgzyd44c5ko8zyh1ya33zccy9gozya112a32izy3252y4333y466zyh354c 110 LCM(22,127)
2985 xp2985_y333yn33zyfooxooyi4r4zyzy54r4z66y5os8gybg8soy566zy913yb31z033yz33zggy5csa7yb7ascy5ggz11yzw11zyfccxcczzy333yn33 96 LCM(15,199)
3358 xp3358_ggybo8gy3ggy37exe7x6a4wccz11yb223y311yfgy2ca23z66ybd97yme909ey2ggzyro8a6yi1074 80 LCM(46,146)
3942 xp3942_y14s0gy1ca23zwoox11z0ok8y14ahhry8dbyaosz8oogyqgos4e6w1zgoo8yd8e13ye31e8zyc62sgy2c453y266 95 LCM(54,146)
4526 xp4526_woox8sipbieeibpis8xoozzwccx8s4c84oo48c4s8xcczy51231111321zypgz2egoyi6511zy679g97zwc453zy433w256xe7x7e 100 LCM(31,146)
4900 xp4900_y88gxc871zy6kug71zy3gs1f5y3ccy28e1e88gz0gs26x12y4ks8y2330311zyqoozwggzw11y6ggzg88c0ccy2132z0117871y233 96 LCM(25,196)
4975 xp4975_yc33y366y333zccyzy5ccy588ge2zye6kkgy4gkk6yi3a8c02zy4ggysggy4o88zy4hhyshhxo489x13zy411ys11w11zyec551y4155cz66yzy566zycooy3ccy3oo 114 LCM(25,199)
5160 xp5160_yy32acyhggzyzy0ggyc643zyzy131zyf8sgzgs26zyfoow354czy54rrrmzy7drrr4zy033 64 LCM(40,129)"""

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

# 124+8n: 22hd reflector with p4 sparkers
p4l1 = lt.pattern("""9bo$8bobo$9bo2$7b5o$o6bo3bo$2o7bo$2o6b3o$bo2b3o4bo$10b2o$2b2o$2b2o3bo$
3bo2bo$3b3o$2bo2bo6b3o$5bo$bo3b2o4bo2bo$2o10b2o$2o$o4$11bo$10bobo$10bo
bo$11bo$15b2o$15bobo$17bo$17b2o""")
p4l2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo4$18bo$17b2o$5b2o10b2o$4bo2bo4b2o3b
o$13bo$4b3o6bo2bo$13b3o$12bo2bo$11bo3b2o$15b2o$7b2o$7bo4b3o2bo$8b3o6b
2o$9bo7b2o$7bo3bo6bo$7b5o2$9bo$8bobo$9bo""")(17,32)

def p4_22hd_loop(p):
    if p%8 != 4 or p < 124:
        return None
    exts = (p-124) // 4
    return (p4l1 + p4l2(exts,exts), 136, "p4 22hd reflector loop")

mold = lt.pattern("3b3o$bob3o$obobo$o2bo$b2o")(-1,15)

def mold_rectifier_loop(p):
    if p%8 != 4 or p < 212:
        return None
    pat, mpop, source = rectifier_loop(p//2)
    return (pat+mold, mpop+12 if mpop != None else None, source + " + mold")

# 64+8n: 6hd reflector with Coe's p8
# https://conwaylife.com/forums/viewtopic.php?f=2&t=5338&start=75#p148210
p8l1 = lt.pattern("""4b2o8b2o$4b2o8bo$15bo$14b2o$3bo9bo$4b2o3b2o2b3o$4bo4b2o5bo$4o11b2o$b2o
$2o7b2o$2o6b2o$2o3b2o3bo$5b2o4$4b2o$3bobo$3bo$2b2o""")
p8l2 = lt.pattern("""13b2o$13bo$11bobo$11b2o4$10b2o$10b2o3b2o$15b2o$15b2o$14b2o$2o11b4o$o5b
2o4bo$b3o2b2o3b2o$3bo9bo$b2o$bo$2bo8b2o$b2o8b2o""")(4,8)

def p8_loop(p):
    if p%8 or p < 64:
        return None
    exts = (p - 64) // 8
    pat = p8l1 + p8l2(exts,exts)
    return (pat, 92, f"p8 6hd reflector loop")

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

hd0_1 = lt.pattern("""17b2o$17bo$18bo$5bo11b2o$5b3o11b2o$8bo8b2o2bo$7b2o9bobo$2b2o7bo4bobob
2o$3bo6bobo3b2o$3bobo4bo2bo$4b2o5b2o2$13bo$12b2o$12bobo2$2b2o$2bo2b2o$
3bob2o$bobo$obo2b4o$o2b2o3bo5b2o$b2o2bo8bo$4b2o9b3o$17bo""")
hd0_2 = lt.pattern("""4bo$4b3o9b2o$7bo8bo2b2o$6b2o5bo3b2o2bo$13b4o2bobo$18bobo$15b2obo$15b2o
2bo$18b2o6$9b2o5b2o$8bo2bo4bobo$4b2o3bobo6bo$2obobo4bo7b2o$bobo9b2o$o
2b2o8bo$b2o11b3o$3b2o11bo$3bo$4bo$3b2o""")(13,11)

def p1_0hd_shuttle(p):
    if p%8 != 6 or p < 118:
        return None
    exts = (p - 118) // 8
    pat = hd0_1 + hd0_2(exts,exts)
    return (pat, 144, f"p1 0hd reflector shuttle")

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

def p6_22hd_loop(p):
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
    return (pat, mpop, f"{n_gliders}G p6 22hd reflector loop")

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

cfuncs = (rectifier_loop, mold_rectifier_loop, p4_22hd_loop, p8_loop, snark_loop, p1_0hd_shuttle,
          pd_shuttle, p6thumb_shuttle, p6_22hd_loop, p14_shuttle, twinbees_shuttle)
