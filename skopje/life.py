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
11 xp11_08k8wg8e13zy13d115b8ozc453 33 diamondback
12 xp12_08ean1e8zoga3zwcikb73 31 LCM(3,4)
12 xp12_0o6gik0a93z1226xcikb73 31 LCM(3,4)
13 xp13_gy1gr3zd5a64210g8c4066zy2kr6og 34 Beluchenko
14 xp14_j9d0d9j 16 tumbler
15 xp15_4r4z4r4 12 pentadecathlon
16 xp16_0c2w3vz33032988 21 Rob
17 xp17_32acy1ca23zy27rszwo8a6y16a8o 36 honey thieves
18 xp18_66625ak8zy177xcc0cczy1g8mwiozx91gp 43 H(bi-block)
18 xp18_wc93xs112ogggzbdhe96kk801zw1213 43 PS(3*5+3,3)
19 xp19_0c4gf9gy4c88gz69alld03xoy11108cy2g8oz0643y2c5y47xg0cabk4ozy9354cy3125t38dzym11 92 H(HF)
20 xp20_35426ow37bkicz65123 30 LCM(4,5)
21 xp21_g8gw3jz01xqpwsszy111wc2w8k8zy566 32 Ø
22 xp22_178cwggg2y2oo4kozy235433y28111w62sg 36 Jason
23 xp23_02egoy1ca23zy4sgox4acga6zgs26y01y239czy3ccx6a8o 55 H(HF)
24 xp24_xsssx4hh186z777y37 24 LCM(3,8)
25 xp25_32aczy0ooj64zy74cp33zyc6a8o 30 30P25
26 xp26_ggy2ooy6ca23z0346xogy5g8gw4ka8z2a54w121y513xc4ozxo8a6y633y211 60 H(HF)
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
38 xp38_y2178czy8s4cy1szsoyfesz01sy1ogszy9o8gzyb32 42 H(R)
39 xp39_xqh2z33173xccz4sk0emicy2oozy469dezy4327 46 LCM(3,13)
40 xp40_33zxs48g69gvzx3021zy833 26 Beluchenko
41 xp41_0c4o0e93y1g88cxo4qajkk8zca2t553gggxhhgx110h21xck8zx11g8oxey425dzy023yzwg0s4zylgy2ra4y0ggg070ggh108ozyk1230ggo4o0o8y08oy2caar453zyn122c5521x311y2c970123 170 H(pi)
42 xp42_033y133zo4maxam4oz1ppy1pp1xgfnzyb1252333 50 LCM(6,14)
43 xp43_y6c88gy832aczy811yl33y2oge2zy2gy6ccgccy3oo4ooy67z0o4cw3z11y433y5o8ya6a8ozyi113 70 H(pi)
44 xp44_0oql96xmqzgh1gxeqaa4oz1011y217871 45 LCM(4,11)
45 xp45_4ahhhhhha4zy94a6zx35c53zy166 29 H(pi)
46 xp46_033y133zzzckgsxsgkczz0cc 28 twin bees shuttle
47 xp47_w32acyeca23zy37y2ccy27z252xeaey8eaex252zg8gxsksy8sksxg8gz01y1oy2ccy2oy11zwggkc01ya10ckggzw1yk1 84 PPS
48 xp48_660259gcy1g8gzy166y1sspxgk2gb3zy8ooy011 44 LCM(6,16)
49 xp49_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66yb1226 44 44P49
50 xp50_y132aczy5ooj64zwg08oy64cp33z320i9802i908oy46a8ozy33201 58 LCM(10,25)
51 xp51_y14a4y1ca23zwggy2gyfoge2z470h8ow25d52yfg0s4zw23wggyd4ara4w11oge2zy04701zyhc453y1252 84 capgun
52 xp52_4s0gy3ca23zw11w4ed3zy08oy362sgzw311 35 H(LOM)
53 xp53_yjca23zyg356yfggkczylcssw66y4643ggwc871zy1ggyw123z0o4c0123g8oy4ooweecz11xca23yfo8gzykggkc011zyk1 94 Riley
54 xp54_y566y2ca23z178cy14ksy6c871zxgozx31yadb 43 H(R)
55 xp55_y0dby06a8gzggci5ld3xogg150cgz0343y523y0346 49 LCM(5,11)
56 xp56_66625dw66zyb66zzy0oow8s26zy61ooo8kkwoozyc1 45 p56 B-heptomino shuttle
57 xp57_y0oggqh2xgzy1pib12gc01156xg8y2oge2zyf3441wooowca6zy2s4oyb347zca6w333wg44oz08e13y221xckgg0618gq9jzyf1x8hb113 112 H(Rt)
58 xp58_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cc 54 H(pi)
58 xp58_y932aczy5ooy3osogzyi76y0cczz33y06eggggy3ggzy5131y311zy9354c 54 54P58
59 xp59_yhbdy139u0o4czygggy3254t2aczyf78dy511zy6gggz6246y132023zo80gwgz01pl55o7k46zy311 86 H(pi)
60 xp60_vtvy037bkicz757 24 LCM(4,15)
61 xp61_yddb8oz0oggmicggkcx6513zca260743zy066y74ehryfok46zy1ggkcyfc4ogy7ggzy11yi321y7gh1g08ozytggxok47o7k55dzyoc88r221y411zyq32 134 H(pi)
62 xp62_ccy069c536635c96y0cczz66y0ci6koccok6icy066zzy4ojd11djo 66 PS(5*12+2,31)
63 xp63_8o6pajkk8z32q921w4a4z321w66y1eh9mzy83443wgw33zyd121 64 PS(12*5+3,21)
64 xp64_y1j3zy031d8ey633zggy6s4c0gz11y8hj1zya11 34 Merzenich
65 xp65_3pmwmp3zxh1gx21h2zx3c7a5301gk2w96zy5admlk 52 LCM(5,13)
66 xp66_y2ca23zws21q4zx11zxgc22szw8o121z311y0681hh4zy77 48 LCM(3,22)
67 xp67_yxo8bp6o8g0s4gozyrggy31230343zys346y133zyz1530ggzyzy01226y4ko8zzyi86cyzy8ok46zxggyzypgy64s0ggzw64lkk8y7g0s4yzy1g8o0123x33xmlld221zok4raa6xccxs48011yzy223y9122qi6zx32y2ggzy56221yzy8361zysggzyr112y464kozyzy4ca8zyzy4ccy162sgzyzgg0s2s0s4owgzyz1023w1169d11 228 8G snark loop
68 xp68_y6o8brz0oggzx23y56c53zgs26zyf354c 38 H(C)
69 xp69_y42egoy1ca23zybsgox4acga6zwgy0gs26y01y239czw1p5ao488ggwccx6a8oz8p78bhc870728cz012521 103 LCM(3,23)
70 xp70_033y133y1o62453zo4maxam4oy132156z1ppy1pp1 52 LCM(5,14)
71 xp71_y1ck8yfc871zz8e13y7gggy3351zy3o4cy012421yh64koy6ggzy211y6354cyhg848gy0643zyugkoy3111y7oge2zzyrgs26yf256 92 dependent reflector loop
72 xp72_3bg2kgzy011y7ok46zy268ga4w8k24ozxo8a6 36 LCM(8,36)
73 xp73_2egoy8o8bdzy8gggy03156zy9243y14a4zzy54a4y1o48zy6ckgoy0111zy9mq23y831e8 68 H(LOM)
74 xp74_y532acy5ca23zggyrggz0346y5636404636y5643zz0o4cy5coc404cocy5c4oz11yr11zy5o8a6y56a8o 84 Raucci
75 xp75_32acy9sksssskszy0ooj64zy74cp33zyc6a8o 42 LCM(15,25)
76 xp76_o4an7y1ca23yi32acz0110888xooxoa6ya6aoxoox888zy47ys7 56 LCM(4,38)
77 xp77_0jjg08c2a2oggcxqmz3w145431wccy3gozya8kkn9b4303213zyd1 67 LCM(7,11)
78 xp78_y45rc31zwmkac48g012640cczw1wgw1rozmkgino3s4z1w6221 61 LCM(6,13)
79 xp79_y232acydqmz4s0gywmqzgg11y5goy9re4y432acz1qa6y4136ykc4oz023y78oydggy211zya32yd1226 80 H(pi)
80 xp80_35426ox22i8o0ooz65123y1vow86 39 LCM(5,16)
81 xp81_yzyzwca23zyzyy33y2eu80gswsg0gzyzyw2a6y4178ewew121zyzyz0o4ozyzyugs26x1zyzyzxco4zyzyca64zzzyzyisg8zyu42ezzzyz08okzya86czyhoge2zyc696z0gxsws4oy5okgz1212ewe205vsy2ggzyaggkc011zya1 146 p3 22hd reflector loop
82 xp82_013320444y033y8oozy94emozzzy83de4z33y8ooy044408oog 48 H(LOM)
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
94 xp94_y933zxggyk66y0o8zx1y359b6y4ggy4321zgs26ye3645y28czy233zyi66 54 H(pi)
95 xp95_0c4gf9gy4c88gy2o8wo4oz69alld03xoy11108cy011j8n495m88cz0643y2c5y47xg0cabchci8fgra96zy9354cy3125t38r221zyo11 141 LCM(5,19)
96 xp96_0178cy766zy44koy6m640ooe4a4z0gs26x11xoy1oo022440ezo8go 59 capgun + boat-bit
97 xp97_ydg88e1u8y533z0kcyb11313kzol56y1ca52y6115137zy4ggyp2552sgzy411y94ocx6a8ozyzxe24zzzzyzy448ezyzyg32acx634y9ggzyzy4178kk8yp11zyzyksogkggy68ka6y1ckl3zyzyp5ogoggyb65zyzyeooy52fge221 164 syringe-rectifier loop
98 xp98_64wo0k297x66zo8w60ag4oxoozy411y6ccybg88czy1ccy2628o8y38c80gy2op1zwo8a6ybooy111 78 LCM(14,49)
99 xp99_wg8o696o8a6zg1aq1qr6wccx6ioz11074wo80gxeqaa4ozy511y217871 75 LCM(9,11)
100 xp100_32aczy0ooj64zg88gy34cp33z125eey76a8o 42 LCM(4,25)
101 xp101_y0ggy58oy23lk2mkk8zy1346y4123y11101zy6ggygoozy46761ygcecy3c871z8e13y33njygome6zy811zycggo0ooy1c4oy462sgzyb122642acy211 116 116P101
102 xp102_ybc453zyeg8w4kk8y2gg8kbw9czy1ooy678c48by5408czooog8lb4zy01yeggozyi32 67 Raucci
103 xp103_yzyzyv33y58e1e88gzyzyzyzy3330311ybckzyzyzyz03224e6y725acy165lozyzyzylgs2552ypggzyzyzyxo8a6yf11zyzyzyma64y8742zzzzzyzyz4kcy86c2zzzzzyzy9gcoy8ca8zzzzzymg8oy88okzyo1ok46zy433ypg88ge2z6a8oy1ck8gy7os8gggy611z0bdy41y4g0ggy11zyd255t0t5y5ggzyh1y711 180 syringe-rectifier loop
104 xp104_gk2gb3y013cr5z11y0cc046210g84cakmzy8or1y11 46 LCM(8,13)
105 xp105_o08cbb2408fvy2skszff1024dd3101y2vnv 46 LCM(7,15)
106 xp106_y0133204440gcg8z8oy91z0123y14c4z178cy1252y131e8zydc4ozy0gg8y811zy1211w7wc2gc 66 H(TB)
107 xp107_y232acysooz06a8oyloge2y9g0s4zccy3sqa4yu11zwggyu4ab7y366z4701y98e13yl32aczy333ys6a8o 86 H(R)
108 xp108_8o6pajkk8z32q921y8ca23z321y1131y08c8zy0c453 54 PS(21*5+3,36)
110 xp110_c4oy1178cwggg2y2oo4kozx160kgy235433y28111w62sgzy412ac 51 LCM(5,22)
111 xp111_x8a0t1e8zwok771g88gzy4121yl6is0g8oz628s0s4y079eyceisy0470728cz0321079cylg8gzyt1221 91 LCM(3,37)
112 xp112_om999e0e999mozx8kc0ck8zzw8if505fi8 50 LCM(14,16)
113 xp113_ggy666y0c871z0346zy8gggy7cczy83wbow330oowoozzy9ggwggy1gzy911w110ccw1dggszy933zyx62sgzyf8e13y066 86 capgun
114 xp114_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zye4hh186zyf7 57 LCM(3,38)
115 xp115_y032acx66zw6ioy2gy0c871zca16a4x317zy2o8a6y0gbbgn1e808ozya11mq0v5kk8zye343 93 LCM(5,23)
116 xp116_y6o4an7zy711zy166y5ok4kozym31e8zx32acyc6a8oz2egozy535453y5cc 68 LCM(4,58)
117 xp117_wg8o696o8a6zg1aq1qr6wccz11074wgy1gr3zy3d5a64210g8c4066zy9kr6og 76 LCM(9,13)
119 xp119_y3ggyc33y0c88gzy311yk11y8ooz0g8oyfca3acz23yho808oyfc871zwccyg131zyc6a8oyi66zyk33 72 H(pi)
120 xp120_4r4y13bg2kgz4r4y511 24 LCM(8,15)
122 xp122_ymca23zyag8gzyb1yjca230ggz178cxooy7e9h9ayg34a4woozwggyogy9ggzw11w252sgyf59897y711x31e8zy8c453yig8gzyz1zylc453 102 H(R)
124 xp124_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy337bkic 60 LCM(4,31)
126 xp126_ggyhca23y26icgca4z0346yq12303156zyk1rhezyr8ak4 52 H(R)
127 xp127_y932aczy366y4sccy44a4zyd44c5ko8zyh1ya33zccy9gozya112a32izy3252y4333y466zyh354c 74 H(C)
128 xp128_064268e13y4ca23zz66x8c2c8zy8gggwcczxvs61zx11y1oge2c84c 62 H(pi+blinker)
129 xp129_ggyhca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyyc453 38 H(R)
130 xp130_x32acz31e88g0653zy01pgz66w1023y3o8gkcz66w8gkcy23c84kozy08pzc8711w6aczxc453 88 LCM(5,26)
132 xp132_252w253zy0gxggg0ooozy13w3488a61oml1hiswcgzw695qsoy3111zyica4w4a4 72 LCM(4,33)
133 xp133_y932acy2oge2zy2syh33z8e13yb63qszyw31e8zyf2egozyw7bocyboge2zypooyh7zys8e13y26a8o 84 H(B)
135 xp135_y9330gzyb1789azy08q987yfooz33yfs2ib2zy6ai2sgzy910ooy2uquzyjfbf 68 LCM(15,27)
136 xp136_y6rb8oz0oggyhssszx23y56c53y6777zgs26zyf354c 50 LCM(8,68)
138 xp138_w8gw259r84z79431y1go4iszx42rik8w12 36 Gabriel
140 xp140_wgy3ggy332aczw1156y011yogzyic6sgy9121zycggz8k8ya363zyqooy06a8ozyf354c 58 H(O)
141 xp141_x8ean1e8zwoga3xca23y032aczy37y2ccy27z252xeaey8eaex252zg8gxsksy8sksxg8gz01y1oy2ccy2oy11zy310ckggy0ggkc01zy81y01 103 LCM(3,47)
143 xp143_xgbb88gzy1cd3gv04aczc4530gy1gr3zy1d5a64210g8c4066zy7kr6og 69 LCM(11,13)
144 xp144_33y18kk8yb33zy8equzy9757wggzccyb1221y1cc 42 Achim
145 xp145_w3pmwmp3zy111y1ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11zzy8252y1252 72 LCM(5,29)
146 xp146_4s0gyie7zw11y2ei0iezwo8a6y21zy466w4acxsexes 51 H(pi)
147 xp147_178cwoozzy3uey1s112ogggzggx451xoox1z11xoa2zy077zy1ggzy111w31e8 56 LCM(3,49)
148 xp148_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701x888gy0354czxca2ro8g2i0sz031132y11 89 LCM(4,37)
150 xp150_w178cxg8zy417gukzy75f1sgzccb7w66y121x62sgz066 46 LCM(6,25)
152 xp152_y2178czy8s4cy1szsoyfesz01sy1ogszy9o8gzgggeeey532z333 54 LCM(8,38)
154 xp154_gjjy1jjgz34daxad43z0ooy1ooy2ok4ooy22gggwc871zy6gs26w1118y233453 70 LCM(14,22)
154 xp154_o08cbb2408fvzff1024dd3101y1ok4ooy22gggwc871zy7gs26w1118y233453 70 LCM(7,22)
155 xp155_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2idiidizy31w1 64 LCM(5,31)
156 xp156_og8o0e93y266zx32wom5hley266zy312221y466zya6a8o033dew66 66 LCM(6,52)
158 xp158_ykc871ggzyo11y0oge2zy233y8ra4zysmm0mp3zyt343zz0oe1e8z643033y6goz0g8oy7126y866z23y2ccwggzy64701 96 H(pi)
159 xp159_yqgbb8ozyk64130343zzy67zyz33zwgg0444y5747yhc871z4701yh717y5111zy066zyu7zzy6oggm9606413zy866 90 H(pi)
160 xp160_y42egoy533z0oggzx23ye8sky3cczz66y3572yeo8zyr113zy8ooy531e8 56 H(pi)
164 xp164_013320444y033y8oozy94emozyoj5gskkzyned541023zy83de4z33y8ooy044408oog 70 LCM(4,82)
165 xp165_y0dbzggci5ld3xog8oz0343zy275777757 45 LCM(11,15)
166 xp166_y031e8zwo8b513z0ggo0ooy444sy4ooz122ege2y123011zypo4ozy3ccy4sii031y1dd0d552zypg88czynbq23zyo123 102 H(R)
168 xp168_0g8gw3jzw1xqpwsszy211wc2w8k8zgggeeey066z333 44 LCM(8,21)
170 xp170_y6438g0ia4zx66w66xac4zxggo4c4oggyh66x66zca16888188861acya358mhh181hhm853zy066x66yj12321zyv66w66zym252x66 119 p5 shuttle
172 xp172_y833y033z8oyoo8z0123y2757y2757y2321zzz0g8oy2sksy2sksy2o8gz23yo32zy8ooy0ooy4k0il96zyp1 88 LCM(4,86)
174 xp174_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cczzy9oiwm8gzyepg19 72 LCM(6,58)
175 xp175_32aczy0ooj64zy74cp33zyc6a8ozy3mf0g066zy235t0bqczy166xf6 64 LCM(7,25)
176 xp176_y2ca23zws21q4zx11zxgc22szw8o121z311y125202vjq7zy72e841 59 LCM(16,22)
177 xp177_y3343x6bacy6cab6x343zkk8yy8kkzgo8gywg8ogz0123yw321zzgo4syws4ogzgh1yy1hgz221yy122zy3c2cx6d53y635d6xc2c 104 Karel
177 xp177_y8guy3178cxszy5618882zwgggybsk2ccgzw8oy4oo4ooy1333z311y4164611y5ss3pr4y3ok46zyd8mm68oy11y5888zye11211zyaoxggzya1x1074 104 LCM(3,59)
182 xp182_x32acz31e88g0653zy01pgz66w1023z66w8gkcy366wgo4k4gwozy08py461138a86201ppzc8711w6aczxc453 104 LCM(7,26)
184 xp184_33y7cccd72ycssszccy7333be4y4ccy5777 40 LCM(8,46)
185 xp185_ya3pmwmp3zy432acy111y0oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354c 76 LCM(5,37)
186 xp186_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy0ccb7w66zy166 64 LCM(6,31)
187 xp187_ygoggydca23zyi23zyb4s0gy63d8ezyd11yj62sgzzy6o4ozy3255d0ddzysbr0raa4zyt121zggz0346yjo8gzy971bcy832zyickggzwc453yf1 112 H(C)
188 xp188_y8o8y1ca23zyj66zxooy4eoiczzydo4coy4ccz695qsoxggy3101zy511w8oy18czy7311 68 LCM(4,94)
189 xp189_y9g033zy6a9871zooyf789q8zy02bi2syf330oozybgs2iay24a4zy9oo01y96995a996zyvggw252zyv11 88 LCM(21,27)
190 xp190_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zy9i6vwv6izy911y011 62 LCM(5,38)
192 xp192_064268e13y1ggzya11z66y1sczxsmeiy1gggwcczzy6oge2c84cz33 59 H(pi+blinker)
196 xp196_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66y5eek8g01226zyq1221 56 LCM(4,49)
198 xp198_32aczx4q12sy433088ehjzy111y1c89aq2v1kd221zws22cgy332x1zx121o8zy3113 78 LCM(9,22)
199 xp199_yc33y366y333zccyzy5cczye6kkgy4gkk6zy4ggysggzy4hhyshhzy411ys11zyec551y4155cz66yzy566zycooy3ccy3oo 84 H(LOM)
200 xp200_32aczy0ooj64zy74cp33zyc6a8ozy2gggeeezy2333 42 LCM(8,25)
201 xp201_y9ca23ydggy2gzy033yaccc08gy411x6511wg88czyk631ye11y7o8zyzyd321z0g8oz23y7ggyegoczy76221wggkcxggy4120666yaoozyd1y211ydo8a6 98 capgun
203 xp203_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11wggzyng99o0k6hl1c886zy8252y1252y01x2221x66 88 LCM(7,29)
204 xp204_y6rb8oz0oggzx23y56c53y2gmugg0gzgs26yh111w21zyf354c 50 LCM(3,68)
210 xp210_033y133y3gcgzo4maxam4oy2gfgz1ppy1pp1y33 46 LCM(14,15)
212 xp212_gy332acw32acz37gy4gxogy633w2doa080kczwjg8y231w621y5ggy0c9626zx211wggkcwggkcy511zy41y11 82 LCM(4,106)
215 xp215_g8gg8gx8k8y18kie0mp3y0oge2z4b44b4ylg0s4zy1ggx1ppy8jjgx11zx4701zy18e13y0ojd0e952y1252 96 LCM(5,43)
216 xp216_y332acy266zw178cy6sk4y1c871z0ccygogz6om2yf13z033 52 LCM(8,54)
217 xp217_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2660g0fmzy3cqb0t53zy46fx66 82 LCM(7,31)
220 xp220_ya32acy06a4zysoge2zo8goy04aicy5771332y5cik8y06246zy8gs26zyj8koy0ckggzyt1 74 H(HF)
222 xp222_2egoy7ca23zy56bb4y8ggzgs26yf643zya2dd6x66xcczy4c453y966qswcc 67 LCM(6,37)
225 xp225_y432aczy8ooj64zy5ggy44cp33z4s0gy0grqjy86a8ozwhhweh040hz4701y01rbpzy511 78 LCM(9,25)
226 xp226_yfbdz8oy633z0123zyfggy166zy9ss8x1409cwcczyb33zy9oowo80gx3bsszy9ggx2046zy911zyx31e8zygo8y133zyg23 84 capgun + boat-bit
228 xp228_yog8ka37acz32acyj37aczwsy1sy7sb4zy0222zyackgossssogkczy83552y42553 73 LCM(6,76)
230 xp230_033y133zzzckgsxsgkczzy4cczxggzojdwdjo 46 LCM(5,46)
231 xp231_8ehe8oy1o8a6zw12ll64y04a4zy056x66y1eh9mzyc3443wgw33zyh121 66 LCM(11,21)
232 xp232_y8ca23z252y24eexcczg8gy28ssy366xg0s4z01y76e6x6e6w11z0gggeeez0333y4252y1252 66 LCM(8,29)
232 xp232_y53bg2kgzy911zzy5ok4koy566z8e13zxo8a6ycca23zymoge2zy1ccy535453 66 LCM(8,58)
235 xp235_3pmwmp3x8k8y18k8y4ggzx110gggybggg0643z0gs26y3cecxceczy466y966zy2gggx373x373xgggz0gs26y3gy3gy362sgzy7121y1121 102 LCM(5,47)
240 xp240_4r4y11h94c0ccz4r4y2fcw43 33 LCM(15,16)
245 xp245_y2idiidiz32acx1w1xgy033y1ogzx66y2co03y5ew1y23jgzye66yb1226 60 LCM(5,49)
246 xp246_gy1660259gcy7ooz37gy466zw3z66y0cekoy635e6y0cczynozyn1sozx33yk1 64 LCM(6,82)
248 xp248_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zssszx777 60 LCM(8,31)
250 xp250_y1ooy2o4a9jwggzy1ccy0elh4wrwhhz33x6a2y134aipw11z252zzzzykggy94a4zygoowp452sgy6cczygoowtw2oa7y0jjzykc9521y211 119 p5 shuttle
252 xp252_vf8042bbc80oz1013dd4201ffyaca23zyc131y08c8zy8c453 56 LCM(7,36)
256 xp256_064268e13yacczyhcib6x40tckoz66xca2acya4a4y011501zy8gggwccz0cubl76zx11y1oge2c84c 86 H(pi+blinker)
258 xp258_xggyhca23zy0346ycggzyi13zcg952066yygs8z066yzyi62sgzyzwc453 54 LCM(6,129)
259 xp259_660g0fmz0cqb0t53zw6fx66y0g88czy466x11zy3ceicy7c871zxo4cy7cisczw11zy7c453y2354c 85 LCM(7,37)
261 xp261_y88k8y18k8wo8b9c0cikozyo334728q552z0gy7cecxcecwggx33x123z121y2277y3ccx1074z8k8y24eex66zy86a8o 96 LCM(9,29)
264 xp264_252y2gycggz652y2o99gy5oq1851zy4stgc87zy6s261n7zy71ii3y28kczya1y28k8 72 LCM(8,33)
265 xp265_y83pmwmp3y064kozy1o8y411y7ca6z2egow1178cy4cc8goczy1653zymgo8gggy4gg06530o8gzyhggx1x11y41074kox32zyg321o8zyk113 112 LCM(5,53)
266 xp266_yeey0c871zya111cczyd4cgozgjjy1jjgz34daxad43z0ooy1ooy5ggzyd2301zya88833zye7y031e8 78 LCM(14,38)
266 xp266_33j71t8ggz678u0h431zx223333wssgyogsszy47y4259e4y84e952y47zy2o8a6yw6a8o 78 LCM(7,38)
272 xp272_y6rb8oz0oggyhszx23y5e8d3y3gecrar1zgs26yh61w1zyf354c 60 LCM(16,68)
273 xp273_yjmf0g066zy4o4cy735t0bqczx321f811y766xf6zyio8gwooz6246y2636y61oggzyaggy3sd4pzya11x66x110ciqs0ae8zylcc 111 LCM(7,39)
275 xp275_y132aczy0ggxooj64z6246kh88y44cp33zcc0fip6sgnsy66a8ozy2346 71 LCM(11,25)
276 xp276_y6719ezo44cz111yac997zy3s40ozy4111y4qq1ckq4zyg1266061 60 LCM(4,138)
279 xp279_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy16a8850cs1v0cczy36519e121 84 LCM(9,31)
280 xp280_x352y364koz0ccx4r7y4gcgxoozy5ckggy033wgzgk2gb3y21y3123z11 56 LCM(8,35)
282 xp282_xgjjzx1167w33y766zggy0ccz0346yecmiay213zxogy2a9d6yec4ozyp66y011zy9cc 72 LCM(6,94)
286 xp286_y2ok4ooy22gggwc871zgs26w1118y233453y1s8ozylemiczyh33y269de0574zyn66 70 LCM(13,22)
292 xp292_4s0gyie7zw11y2ei0iezwo8a6y21ybg8k4ozy466w4acxsexesw25041 63 LCM(4,146)
294 xp294_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66y1ggcswoow1226zyl1pp 60 LCM(6,49)
295 xp295_yg178cy0ca23zggz0346ybeahmm8zggkcy2gcc2ssy1111xgggz1y6323y7eehcd2y2ca23zwg8gg8gy44rr3ksybo8gzw4b44b4y71yf32zy5ggkcy0c4ozy51y511 124 LCM(5,59)
296 xp296_y632acy7oge2zwggy84bb6zx346yf62sgz0ccx66x6dd2z6om2y9354cz033 66 LCM(8,37)
297 xp297_y2o4cyag033z660u13grpd3y5a9871zc84c5h23wooyf789q8zy011y42bi2syf33zylgs2iazyjoo01 97 LCM(11,27)
301 xp301_y6c88gy832aczy811yl33y2oge2zy2gy6ccgccy3oo4ooy67z0o4cw3z11y433y5o8ya6a8ozy8mf0g066x113zy735t0bqczy666xf6 104 LCM(7,43)
304 xp304_32acywca23z0888xooxoa6ya6aoxoox888zy17ys7zyc25202vjq7zyf2e841 65 LCM(16,38)
310 xp310_og8o0u1eoy5ooy3oozy0mlgrzx1qa2my2ov324sy3s423voz62460v0t6y13vo847y3748ov3zy21zye33y333 103 LCM(10,31)
312 xp312_yg33zy1g8gy6ieyag8gzy1121ym121zy2ogg8z33yq844cy033zzy1696yao4y6696zyi11zyg33 60 capgun + boat-bit
318 xp318_y0133204440gcg8z8oy91xo8zgh23y1q2qy132hgz0346y1252y1643zyecczy0gg8y661ik80cczy1211w7wc2gc 83 LCM(6,106)
320 xp320_y13pmwmp3zy411y0cczcczx226wosr73wc88zyf66zy166 52 LCM(5,64)
321 xp321_y232acysooz06a8oyloge2y9g0s4zccy3sqa4yu11zwggyu4ab7y366z4701y98e13y2gye32aczy333yd7f233y66a8ozyl121 98 LCM(3,107)
322 xp322_033y133zo4maxam4oy1ooy1ooz1ppy1pp1zzzyb3547x7453zzyj33 62 LCM(14,46)
322 xp322_660g0fmz0cqb0t53zw6fx66zy2ooybc4ozyjhhhzy233yb643y333 62 LCM(7,46)
325 xp325_0gs2ibaa4y5o8zlm0mlluy2sse321y3ca23z25s16a98gy846joozx11311y233pc4zy6o8a6 96 LCM(13,25)
328 xp328_x33yjsezynezggy0gcmcy7gcgy0ooz11y13y8363z0g7z73yjccy0ssszyu777 60 LCM(8,82)
330 xp330_178cwggg2y2oo4kozy235433y28111w62sgzz4evy2ve4 48 LCM(15,22)
333 xp333_2egoy7ca23zy56bb4y8ggzgs26yf643wg88gzya2dd6x66x62adhhzy4c453y66a88bbahe21zyj33w32 94 LCM(9,37)
336 xp336_8oymca23z0123ya4b97zy9siq4yao8gzxo8a6ym32zyd4a404u6kezyg4sh93 65 LCM(16,84)
340 xp340_y6rb8oz0oggzx23y56c53y2g8gg8gzgs26yg4b44b4zyf354c 54 LCM(5,68)
342 xp342_xok2s0c9b8oz255q826033y5ggz0321x33y4643zy2ey162ezy0e7yfsezyce8cy1ezy7o4czy611 84 LCM(9,38)
344 xp344_y8c88gy832acz3bg2kgy411yl33y2oge2zy011wgy6ccgccy3oo4ooy67zxo4cw3zw11y433y5o8ya6a8ozyk113 82 LCM(8,43)
345 xp345_y04r4ycg8gzy04r4y4gy41zy86511y2om8z252y144accy0gcgw11y031e8zya44a2u7k522zy2178cy0oox3y133522y14a4zy9161y2o8a6zy8g8gzy91 104 LCM(15,23)
351 xp351_y9g033zy6a9871zooyf789q8zy02bi2syf33xcczybgs2iay14sk0emicy2oozy9oo01yc69dezyt327 90 LCM(13,27)
360 xp360_y94evy2ve4zyn4a6zyc27dod72zxsssy877z777 41 LCM(8,45)
368 xp368_y2gy432aczy12251zzggyp62sgz56yc65134w16zyn4o68zy8o8go 48 capgun + boat-bit
370 xp370_2egoy7ca23zy56bb4y8ggzgs26yf643y04ka8zya2dd6x66xccc4ak8g086o4zy4c453y44ka8w6acwefzyl86o4 97 LCM(10,37)
371 xp371_yjca23zyg356yfggkczylcssw66y4643ggwc871zy1ggyvg123z0o4c0123g8oy4ooweecy7330o0nrgz11xca23yfo8gy36dl0e21zykggkc011y437x33zyk1 128 LCM(7,53)
376 xp376_3bg2kgy4cczy011ykoozy062y2k4coyec871zwg8oy411y4cqiky3gz023y0ccyk11zyjoo 66 LCM(8,94)
378 xp378_yd32acy266zy8178cy6sk4y1c871zgx888gxccygogz1ii305chlg622cyf13z011 71 LCM(7,54)
380 xp380_ye3pmwmp3zcieg8oyb11z0suvy5sg2a4zg9jfgoz123zy7s0111zy9222x31e8 75 LCM(5,76)
381 xp381_xguydca23z618882w4a4y1oocmey566zyc8sc0326z033zyigyacczyd64cg3jhzy466y576311y1252zyac453 86 LCM(3,127)
384 xp384_064268e13zz66y1sczxsmeiy1gggwcczzy6oge2c84c 51 H(pi+blinker)
385 xp385_xgbb88g0tb0gzca2t597432wh98cy34a6zx12y311y168c8xoozy033x1316y18ozy2652y3311 85 LCM(11,35)
387 xp387_y3o487p8a6zggw330f860743156y2ca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyyc453 74 LCM(9,129)
392 xp392_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66yb1226zwgk2gb3zw11 56 LCM(8,49)
407 xp407_yc32acy7oge2zy4ggy84bb6zgg0g4cx346yf62sgz101p542mgx66x6dd2z330347o6l56y8354czy311 92 LCM(11,37)
408 xp408_y33bg2kgy5ckggzgggg8gy111y81z11101qt2y3259142sszy111y7111y7ig1jzyu12dw93zyb32ac 79 LCM(8,102)
414 xp414_w6a897o4oz6511a0338f033zy0ooybc4ozyhhhhzy033yb643y333 64 LCM(9,46)
415 xp415_ye178cy3oge2zy8354czxg8gy5gg0ogx4c244y54a4zxghy81y5oggzojdwdjoxo4cy3o8gy123zy611y732 80 LCM(5,83)
418 xp418_y1ca23yi32aczsy48kie4y84eik8y4szx771yo177zygg88ggy24y1oge2zybo4cw332h1y1669b7zya11 82 LCM(22,38)
423 xp423_8oy3nl6z0123ws21913y6gy3gz8e13x12mmjy5121y1121y2oge2zy5321g8ow7y0373x373y07zy723y1ooy9oozzy8g8ow7y0676x676y07wo8gzy723y44a4y14a4y432 132 LCM(9,47)
424 xp424_y06186wswgg8zggy8211z0346y1868z2egoy1787y162sgzydo8gzy1ooy3oox32zzy73bg2kgzyb11 71 LCM(8,106)
428 xp428_y232acy7cia4oycooz06a8oye2021xoge2y9g0s4zccy3sqa4yu11zwggyu4ab7y366z4701y98e13yl32aczy333ys6a8o 98 LCM(4,107)
429 xp429_8k8yh33gzo47y037es8y266w8653g80676211z01w33xbsey74uezy9gy53zy87jdxccw8gzy8137ecy0ei1zyh121 94 LCM(13,33)
430 xp430_idiidiy5ccy0ccz01w1zx178cy2sksy2sksy2c871zzzy9gggy2gggzx8e13y2323y2323y231e8zzyb33y033 92 LCM(5,86)
432 xp432_xogyamqxdv9ae2gkozx13yf4a4x1zgs26y1457y662sgzy5ccy26a8o 64 LCM(16,54)
434 xp434_w33y333y5ccy1ccz86c8y38c68y2cmkgxgkmcz9fy7f9y6202z1631y31361y333y133zwccy3cc 82 LCM(14,31)
438 xp438_y4oow8kcxesxsexcg952066zw64koyj66zy6si1isz8e13yisozyn1 67 LCM(6,146)
440 xp440_32acy866zx4q12sy7ggy0oq186zy111y561851zws22cgyh66zx121o8zy3113 62 LCM(22,40)
441 xp441_032acy6gy033y1ogzy066y2co03y5ew1y23jgzgg0s4ya66yb1226z1gab83r8w66zw123cic32ac 86 LCM(9,49)
448 xp448_gjjy1jjgy266z34daxad43y9skh72w66z0ooy1ooy488ozy833w27411zym33 68 LCM(14,64)
452 xp452_ya32aczzy7ccy48giq2y9ooy0oozyi111y02552y2cczyoccy2g88gyf3123z3123y1o4an7y466y066y311y0gnj34y4cczy611zyzy8ckggzyzyb1 100 LCM(4,113)
455 xp455_ggy533y1ca230ggz0346yd643y0g0s4zy94rghey611zxo80ggzxg99gp6zx11y2ggy6eh1r4zy54701y0o4cydc4ozyc110o8a6y1ooy511 102 LCM(5,91)
460 xp460_yc33y133zzzybckgsxsgkczzggw3jy6ccz11w1ih8kbh1m8zy134485 62 LCM(20,46)
465 xp465_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy3skssssks 60 LCM(15,31)
470 xp470_y23pmwmp3zy511y733z8oy066ykggz0123y4ggy46b95y31zxc8y25463ye62sgzyp33zy966 72 LCM(5,94)
476 xp476_y6rb8oz0oggzx23y56c53zgs26zy34cxece2ko0354czy3gs246p496246zy711 75 LCM(7,68)
480 xp480_y5osq596z4r4y7oy0c871z4r4y6525zy366zy3gggeeezy3333 57 LCM(15,32)
481 xp481_2egoy7ca23zy56bb4y8ggzgs26yf643zya2dd6x66wcczy4c453y3ooy2cime0ks4zyjed96zyk723 85 LCM(13,37)
490 xp490_032acy6gy033y1ogzy066y2co03y5ew1y23jgzyf66yb1226z8kkmhm2s4s0s4s2mhmkk8zxmq01101210110qm 99 LCM(10,49)
492 xp492_0cu5jzx125ce53yqo8zyh25y2ooy523zzwggyck676sogy862sgz4701yd3301zyscczyr61ik80cc 78 capgun + boat-bit
494 xp494_y1gy432acywca23zg8e1pl552y2888xooxoa6ya6aoxoox888zar0raavy2eesgg07ys7z12egjlkk8y31074zy11 110 LCM(13,38)
496 xp496_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy2oo0o8i22zy368wov 69 LCM(16,31)
506 xp506_32acz0gwemicy366zy111zwo6mow4y16517x7156zx111o8zy3113zybooy1oo 66 LCM(22,46)
508 xp508_y2osq596xoozzy2252yi33zy8gcogyfoge2zwggxee810f2y5gg4v08177z4701yg13zy2ccyi4a4zyiggzyi11 86 LCM(4,127)
516 xp516_ggyhca23z0346ycggzyf13zyzy0gs8zyzyi62sgzyp37bkicxc453 50 LCM(4,129)
518 xp518_2egoy7ca23zy56bb4y8ggzgs26yf6430ooy1oozya2dd6x66y3808zy4c453ya6d51x15d6zyn66y166 85 LCM(14,37)
528 xp528_252y2gy9cgwgz652y2o99gy61e6rargzy4stgc87y57zy6s261n7zy71ii3y28kczya1y28k8 81 LCM(16,33)
528 xp528_0qr10330jmz06c0cc08d5y1178cwggg2y2oo4kozy9o88y135433y28111w62sgzxgggy311zsss333 81 LCM(22,48)
530 xp530_y06186wswgg8zggy8211z0346y1868z2egoy1787y162sgzydo8gzy1ooy3oox32zy4ggzy1ojdwdjo 77 LCM(5,106)
532 xp532_033y133zo4maxam4oylg88cz1ppy1pp1yggy01hzyf557y53088803zyaggy4ggzy8ckla26eeee62alkc 91 LCM(14,76)
535 xp535_y232acy8idiidiyaooz06a8oye1w1xoge2y9g0s4zccy3sqa4yu11zwggyu4ab7y366z4701y98e13yl32aczy333ys6a8o 102 LCM(5,107)
550 xp550_32aczy0ooj64zy74cp33zw32acy66a8ozy14q12szy311zy0s22cgzy1121o8zy5113 66 LCM(22,25)
552 xp552_x48r952wg8zsi4ogy113497zw21w8kir24zyjssszym777 48 LCM(8,138)
560 xp560_y4ok46y3253zooxgcgy47r4xcczxgw33y0ggkczw321y3108k84a1a4w66zyfssszyc777 72 LCM(16,35)
565 xp565_ggy666y0c871z0346zy8gggy7cczw6a84cgy03wbow330oowoozwca2461zy9ggwggy1gzy911w110ccw1dggszy933zyx62sgzyf8e13y066 104 LCM(5,113)
570 xp570_y2178czy8s4cy1szsoyfesz01sy1ogszy9o8gzyb32zy5vtvzy5757 54 LCM(15,38)
584 xp584_y4ccw4a6x7exe7zw32acy2gzwggy2e909ez4701yieszzybssszy8777 64 LCM(8,146)
592 xp592_y432acy7oge2zggy84bb6z0346yf62sgzwggy16dd2z4701y7354czx33x77304a4zy36m048zy51033 86 LCM(16,37)
594 xp594_ya32acy266z64koy1178cy6sk4y1c871zx8k24oyiogzy01221yi13zwo44ozw1242hgzy21226 73 LCM(22,54)
597 xp597_yc33y366y333zccyzy5cczye6kkgy4gkk6ye44mg2637zy4ggysggy71zy4hhyshhzy411ys11zyec551y4155cz66yzy566zycooy3ccy3oo 96 LCM(3,199)
616 xp616_y066w3b8896zy9oieew66zzoggy1oozw23g8gy4oowccw4ozx16887y81111zxggzw78gb4zy26a8o 81 LCM(22,56)
635 xp635_y2g0k413y6ok46zwo0a0208k8y1ggocsy5ccz32yahpo164cz066ya1zyxoozydc8o0672zy4ccy5ed633y14a4zyao8a6 89 LCM(5,127)
638 xp638_y166y5si1iszym31e8zx32acyc6a8oz2egozy579g97y5cczygggozycg8g32zyb78861zyeggzyc4bg87zy9o8a6 92 LCM(22,58)
645 xp645_y232aczz4r4z4r4y5gzxg8oy1311zw23zzypo8zyfggoy1321zyg1zzzyj6a8o 50 LCM(15,129)
651 xp651_w33y333yeg8oz86c8y38c68ybqb8oz9fy7f9y569e4y01226z1631y31361y18k8y6g8gzwccy3ccycggx1zyg32qkgow1343zyioge2 108 LCM(21,31)
658 xp658_w660g0fmzxcqb0t53zy06fx66y7cczy2ooz178cyeoc4ky226zxgy3kiqcy411y4o8gzx11ykccy032zy9oo 88 LCM(7,94)
664 xp664_ye178cy3oge2zy8354czybgg0ogx4c244y533zy033y71y5oggzxsssy1o4cy3o8gy123z777y311y732 74 LCM(8,83)
682 xp682_ccy04ajaeweaja4y0cczz66y04apaeweapa4y066zzy7g88ggy24y1oge2zy2o4cw332h1y1669b7zy111 84 LCM(22,31)
690 xp690_0ooy9vtvzyc757zok4sxs4kozzzz033y133 40 LCM(15,46)
704 xp704_y2ca23zws21q4zx11zxgc22szw8o121y8ccz311wccy447zy977asszyas4y466zy666 72 LCM(22,64)
720 xp720_33y18kk8yb33zy8equyesksssskszy9757wggzccyb1221y1cc 54 LCM(15,144)
730 xp730_4q44q4x7exe7x6a4wccz121121ybgy2ca23zyfe909ey2ggzy2seyi1074 67 LCM(5,146)
735 xp735_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66yb1226zy8skszy8vnv 56 LCM(15,49)
760 xp760_c88gyn33zw11ybgyas48g69gvz01110s0111y325dya3021zyaggy4ggyd33zy8ckla291hh192alkc 83 LCM(40,76)
762 xp762_066yica23z33dew66x4a4y1oocmey566zyf8sc0326zy033zylgyacczyg64cg3jhzy766y576311y1252zydc453 90 LCM(6,127)
770 xp770_y3352y364kozgy0ccx4r7y4gcgxooz1156y5ckggy033wgz08w7rp6y41y3123zzwcjrsw2zy2ckggzy51 80 LCM(22,35)
784 xp784_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66yb1226zy0om999e0e999mozy38kc0ck8 78 LCM(16,49)
791 xp791_yj660g0fmzykcqb0t53y6ok46zyl6fx66zy8ggy0ggy4g8gyboozy811y0ppy264422yaggz32acy766y8oo033y71226z0ooybai913y2ccy0cczzy28ozy0311 120 LCM(7,113)
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
1022 xp1022_y133j71t8ggzy1678u0h431zy4223333zgz37yioge2zy979g97zyi354czxe7x7ex652w33 85 LCM(7,146)
1032 xp1032_yy32acyhggzyzy0ggyc643zyzy131zyf8sgzgs26zy9sssy3354czy6777 50 LCM(8,129)
1078 xp1078_y7ggy133ybca23zwgj3y210262y32328cy266z6221yb66zykok4ooy22gggwc871zyegs26w1118y233453 80 LCM(22,49)
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
2205 xp2205_32acy6gy033y1ogzx66y2co03y5ew1y23jgzye66yb1226zzwgcgzwgfgy2re4x66zx3zy3652 73 LCM(45,49)
2356 xp2356_w33y333z86c8y38c68ynca23z9fy7f9y44bsy7sy1sz1631y31361yk222zwccy3ccy3ckgossssogkczye3552y42553 105 LCM(31,76)
2920 xp2920_x7exe7x6a4wcczybgy2ca23zy9e909ey2ggzseyi1074zzyboozy1aiia6zy3ca99az33 77 LCM(40,146)
2794 xp2794_y932acya178cwggg2y2oo4kozy366y4sccy44a4y235433y28111w62sgzyd44c5ko8zyh1ya33zccy9gozya112a32izy3252y4333y466zyh354c 110 LCM(22,127)
2985 xp2985_y333yn33zyfooxooyi4r4zyzy54r4z66y5os8gybg8soy566zy913yb31z033yz33zggy5csa7yb7ascy5ggz11yzw11zyfccxcczzy333yn33 96 LCM(15,199)
3358 xp3358_ggybo8gy3ggy37exe7x6a4wccz11yb223y311yfgy2ca23z66ybd97yme909ey2ggzyro8a6yi1074 80 LCM(46,146)
3577 xp3577_x32aczykgzy6os8gy5121x39e0o8gozwo8gu2ggx11y7ckoox23zy3346x4a4y71zysggz64koyb66y71226zxccy2og464y34c413y266zyeccyb354c 112 LCM(49,73)
3942 xp3942_y14s0gy1ca23zwoox11z0ok8y14ahhry8dbyaosz8oogyqgos4e6w1zgoo8yd8e13ye31e8zyc2664y2c453y266 94 LCM(54,146)
4526 xp4526_woox8sipbieeibpis8xoozzwccx8s4c84oo48c4s8xcczy51231111321zgz37yioge2zy979g97zyi354czxe7x7ex652w33 99 LCM(31,146)
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
p4l1 = lt.pattern("""2o$bo8bo$bobo6b3o$2b2o2b2o5bo$5bobo4b2o$5bo$5bo2bo2$7b2o$2b2o3bo6b3o$
2bo2b2o$3b3obo5bo2bo$6bo7b2o$3b3o$3bo4$13bo$12bobo$12bobo$13bo$17b2o$
17bobo$19bo$19b2o""")
p4l2 = lt.pattern("""2o$bo$bobo$2b2o$7bo$6bobo$6bobo$7bo4$17bo$15b3o$5b2o7bo$4bo2bo5bob3o$
14b2o2bo$4b3o6bo3b2o$12b2o2$12bo2bo$15bo$7b2o4bobo$7bo5b2o2b2o$8b3o6bo
bo$10bo8bo$19b2o""")(19,27)

def p4_22hd_loop(p):
    if p%8 != 4 or p < 124:
        return None
    exts = (p-124) // 4
    return (p4l1 + p4l2(exts,exts), 116, "p4 22hd reflector loop")

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

cfuncs = (rectifier_loop, p4_22hd_loop, p8_loop, p1_0hd_shuttle,
          pd_shuttle, p6thumb_shuttle, p6_22hd_loop, p14_shuttle, twinbees_shuttle)
