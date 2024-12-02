# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:35:22 2024

@author: adam.davitt
"""
actual_in = [[31594,93577],
[46608,24099],
[78052,70524],
[52680,49933],
[92973,56887],
[55296,47645],
[37186,75116],
[40769,84992],
[35040,60175],
[59499,14847],
[85832,56989],
[42482,70454],
[17095,73110],
[61272,10462],
[32160,16178],
[10808,71006],
[16969,28783],
[36787,98690],
[69808,24612],
[70646,27647],
[89828,72826],
[85186,39903],
[34297,27647],
[30786,62593],
[73378,56989],
[83339,76601],
[98464,20355],
[89441,41559],
[92358,86047],
[95206,21717],
[84009,28783],
[55940,36229],
[16698,40884],
[46170,97497],
[24893,73110],
[78554,74542],
[56610,71703],
[95376,63767],
[73946,25624],
[56696,36949],
[76592,28783],
[34578,66225],
[80399,23808],
[35314,99220],
[78549,28741],
[11683,54174],
[93774,44743],
[79918,11180],
[52152,98690],
[62076,98629],
[65123,38917],
[62326,48511],
[61748,83586],
[36657,77764],
[61263,67461],
[66962,73875],
[86674,71817],
[46123,28574],
[59655,77208],
[49453,84165],
[17554,54805],
[20555,35394],
[30841,27299],
[21596,44289],
[69368,99355],
[28783,13411],
[87971,60011],
[62267,30299],
[72766,15906],
[38285,60197],
[44961,41411],
[77170,49971],
[83412,49278],
[65539,71579],
[75567,70524],
[20999,30341],
[28453,56887],
[45890,73110],
[83293,10498],
[58567,60156],
[34749,97497],
[84145,91460],
[13623,83233],
[30367,36965],
[67444,80554],
[88199,23760],
[18912,71703],
[64205,61459],
[26144,61026],
[14014,61026],
[93772,42669],
[72144,89397],
[95074,88828],
[88153,11178],
[23140,35508],
[58361,97497],
[44555,14532],
[55179,42055],
[29820,97497],
[81369,78773],
[26269,56887],
[50117,61026],
[36125,93644],
[83590,56887],
[32923,89397],
[45316,98690],
[40805,17335],
[56036,93577],
[93994,32813],
[50267,21496],
[92009,61026],
[16538,28959],
[45464,69725],
[78459,89397],
[27573,73725],
[95808,98629],
[58710,50844],
[95114,14847],
[89373,14871],
[46780,56887],
[17256,61825],
[60618,86047],
[83650,69073],
[41559,83790],
[17564,39903],
[14550,56989],
[23102,92228],
[55345,60828],
[86875,10498],
[37879,97182],
[61367,60502],
[28688,43013],
[48378,43197],
[43507,66225],
[97628,45554],
[54911,70524],
[15661,17106],
[63694,66225],
[97976,27344],
[11573,98629],
[50406,27656],
[49682,10462],
[97248,50654],
[39656,80421],
[39325,71703],
[32021,45825],
[54741,16894],
[88638,41559],
[82176,83184],
[42652,56989],
[75463,33173],
[21324,24099],
[87338,13695],
[94541,98523],
[62018,52368],
[11814,69643],
[81981,43506],
[26780,61026],
[73851,42025],
[36776,56882],
[17804,79801],
[36965,37207],
[85693,24597],
[24851,92819],
[99569,58459],
[20032,62547],
[53798,68512],
[84095,69643],
[19845,99255],
[66923,86047],
[32514,28783],
[31254,96726],
[90053,60828],
[56135,86916],
[70373,98232],
[80621,28959],
[44580,59148],
[42499,70524],
[53805,56887],
[99976,73110],
[80765,70128],
[33156,64288],
[96181,77208],
[69462,30341],
[66879,17053],
[58273,51470],
[96628,21179],
[68594,28783],
[98313,16248],
[94100,71703],
[10462,21349],
[50253,41092],
[10768,43783],
[30626,86047],
[45117,87173],
[42129,48453],
[92713,69643],
[15779,28959],
[43952,27647],
[70928,90996],
[23158,70524],
[68214,61026],
[24790,36965],
[89829,56887],
[26545,90823],
[11947,61026],
[42766,60828],
[49506,91207],
[70976,98629],
[77045,21717],
[55646,85009],
[36644,62589],
[42308,90973],
[68516,77764],
[52487,93577],
[35162,25545],
[79549,89397],
[74989,93577],
[82472,73110],
[15062,23436],
[88241,14847],
[74205,10462],
[41729,36965],
[63707,60828],
[89794,24644],
[40255,98629],
[70657,24099],
[71278,81326],
[53290,66225],
[66493,37215],
[16519,98690],
[47712,28783],
[58998,73110],
[68367,28959],
[91367,24099],
[57151,93567],
[27625,57280],
[12772,36965],
[87423,21717],
[82514,24099],
[14847,85340],
[13134,14847],
[93592,95305],
[94034,55327],
[30057,41401],
[64355,61540],
[75872,43149],
[42092,38778],
[54943,34143],
[18701,27647],
[33250,27647],
[68597,12290],
[70010,56989],
[86125,36965],
[91175,65233],
[13392,56989],
[85574,75027],
[75378,78256],
[38499,33161],
[58013,96728],
[82425,19909],
[23327,77208],
[70841,98690],
[17655,16614],
[60973,25354],
[53305,98690],
[20358,93577],
[36898,97497],
[25793,41559],
[11521,22236],
[29437,50127],
[61220,27647],
[13177,16182],
[96584,29570],
[36024,28959],
[99363,24099],
[83768,28959],
[34035,91586],
[55288,10462],
[54172,58575],
[92431,95558],
[66357,88962],
[70769,24099],
[93484,73110],
[94279,27647],
[27363,73110],
[22212,36704],
[64134,40360],
[50602,29149],
[11743,61125],
[63645,97497],
[91658,82280],
[20690,56887],
[61026,36917],
[86722,85068],
[61621,60266],
[49513,66225],
[85513,30341],
[66822,60828],
[51449,98690],
[83878,44486],
[89295,36534],
[73974,10462],
[21111,36965],
[63133,14847],
[73098,46665],
[15337,44436],
[13095,73300],
[76631,70524],
[31711,25547],
[48923,45166],
[63702,52084],
[71983,15211],
[56232,82606],
[87202,86047],
[69730,89012],
[75753,28959],
[95683,89397],
[51948,91005],
[78079,66225],
[13420,28536],
[69643,10462],
[30219,14847],
[48811,69643],
[84189,41239],
[81307,99259],
[45532,29995],
[23354,70524],
[72811,94388],
[30341,83862],
[47425,10804],
[47194,28959],
[34930,18979],
[45480,39540],
[16585,10462],
[90933,71703],
[89397,89159],
[43147,30625],
[55547,70524],
[88415,88828],
[54171,45548],
[52054,57173],
[54586,69960],
[36449,92493],
[17465,21717],
[62422,85849],
[23010,36965],
[85263,13558],
[57875,68711],
[36393,99415],
[45176,14847],
[18934,14847],
[92336,31758],
[79552,29466],
[56058,56989],
[10498,15026],
[92819,28783],
[84268,99456],
[51638,71703],
[76553,10878],
[57917,45538],
[14542,53360],
[98690,49777],
[65862,97497],
[40714,88962],
[31433,83300],
[57458,88828],
[75624,38816],
[29630,29209],
[88648,28783],
[32387,26556],
[91924,64750],
[85866,69643],
[56989,93577],
[33130,70524],
[14061,45960],
[77575,24220],
[52091,24099],
[88164,62321],
[66603,15819],
[31807,31157],
[29116,70524],
[77764,77764],
[14028,36965],
[24403,74189],
[79273,86047],
[34094,48073],
[95921,67461],
[87220,88911],
[71505,46709],
[29528,40340],
[23094,60828],
[84115,86047],
[98696,89397],
[20695,70524],
[64217,81201],
[64604,20316],
[12409,68627],
[22114,60828],
[27647,30379],
[43539,61414],
[63028,71703],
[44403,54135],
[68568,22726],
[71841,88828],
[80218,17181],
[76014,77208],
[35395,60828],
[33310,93577],
[86833,32408],
[64319,97497],
[14762,97497],
[21703,24810],
[95068,25395],
[49059,44428],
[87183,75582],
[61862,59522],
[85674,24099],
[50707,28071],
[44206,86047],
[10646,51895],
[29227,69643],
[20049,22768],
[20948,28959],
[77236,88036],
[39903,69643],
[41212,92819],
[49374,96902],
[67502,11211],
[11342,86091],
[32692,12652],
[55397,24099],
[74244,51775],
[73356,86047],
[64530,22350],
[52051,87711],
[88828,93577],
[69106,28959],
[31221,22122],
[98130,52973],
[53412,23423],
[33461,68095],
[98332,33683],
[69072,74582],
[24080,90769],
[42204,92663],
[44236,98690],
[32803,79886],
[26832,98690],
[62064,68181],
[93433,88081],
[97657,42160],
[98134,84335],
[40198,93513],
[33599,97497],
[11389,58702],
[14619,24099],
[30142,30193],
[91642,14847],
[92866,53578],
[56641,27647],
[92302,17388],
[72521,67616],
[58265,61445],
[70765,97497],
[68320,73110],
[53399,47299],
[34054,98629],
[54398,88962],
[40481,41559],
[57863,64542],
[78556,52977],
[89362,14847],
[88962,86047],
[80804,27647],
[89970,36965],
[78821,24099],
[57847,50940],
[64430,53377],
[90877,24259],
[86846,52051],
[19209,54802],
[82497,42858],
[35529,99096],
[53053,25999],
[42861,24099],
[74230,24099],
[43730,36682],
[77678,79547],
[48396,20916],
[59290,66225],
[40715,28607],
[59318,56989],
[70941,56412],
[33674,98690],
[85712,77175],
[53605,15151],
[17450,13535],
[52174,89574],
[14944,14847],
[97784,28959],
[81304,61026],
[49017,44240],
[84135,27647],
[37728,24099],
[82730,55973],
[76104,21717],
[54287,23462],
[67733,33345],
[10575,39903],
[21252,96655],
[49645,75614],
[77534,73110],
[82071,52051],
[90911,41092],
[98203,36391],
[91832,65483],
[57305,52051],
[78103,79732],
[67461,42766],
[12386,20194],
[20161,86047],
[91604,43190],
[19693,69218],
[21633,76615],
[65299,14847],
[44435,55063],
[78009,89397],
[86479,69643],
[24148,71242],
[64277,64249],
[44127,78140],
[28959,41559],
[45103,80022],
[42451,39903],
[41769,47985],
[72456,95014],
[99085,83622],
[29743,66225],
[23909,18415],
[53844,36965],
[54787,38120],
[36391,36965],
[63368,72209],
[14000,27647],
[80901,82335],
[45078,26197],
[10736,98690],
[83348,28783],
[15797,69643],
[67439,97497],
[59007,98629],
[41737,79601],
[22845,27027],
[97641,90133],
[27794,89410],
[64042,69643],
[85778,87090],
[99918,52976],
[75669,67881],
[61506,10498],
[33813,86047],
[55160,50599],
[76454,97497],
[58135,86047],
[62079,41092],
[38282,85091],
[56570,27647],
[20868,39903],
[44191,70450],
[68472,77208],
[63686,41146],
[87459,21717],
[32659,87632],
[64174,97497],
[11135,56580],
[11199,83300],
[84581,49788],
[89243,14847],
[29266,56887],
[15752,76150],
[25107,29800],
[54903,61073],
[14590,88828],
[41987,42766],
[24099,21717],
[40661,80319],
[25665,20728],
[57002,28783],
[22313,71781],
[17735,39602],
[71925,36965],
[38910,16700],
[85767,93240],
[69424,30341],
[60863,73110],
[95233,29246],
[42390,28959],
[19291,73769],
[47356,48551],
[50683,66225],
[84500,41624],
[79030,89397],
[87533,41092],
[23830,21331],
[19336,42039],
[46633,69816],
[25279,88828],
[94682,30341],
[64240,86047],
[43665,28783],
[54720,56887],
[27128,56589],
[48036,28735],
[71202,60660],
[94253,85389],
[66231,28046],
[27862,38375],
[65097,85050],
[30614,39903],
[79606,49477],
[10785,51809],
[21201,67461],
[90921,24099],
[43970,44782],
[58040,73110],
[14615,60837],
[29984,95967],
[76018,84043],
[58650,88828],
[36399,27647],
[46171,36965],
[86063,77764],
[55705,36965],
[21694,45407],
[38204,64750],
[91565,37548],
[77459,85298],
[36117,14847],
[93436,32602],
[35033,43588],
[99044,33084],
[65014,60011],
[16701,71703],
[64364,76350],
[70681,24099],
[97497,81759],
[11614,10462],
[18793,63401],
[30187,35388],
[77263,24883],
[48188,64450],
[60290,10462],
[17278,71732],
[68842,89669],
[99638,13496],
[76856,93577],
[47431,45435],
[63788,77747],
[41116,77208],
[12911,52051],
[32338,23771],
[78235,73110],
[87883,55995],
[73451,28724],
[66586,77208],
[23406,48109],
[90035,56989],
[79303,77208],
[79348,47799],
[66202,36965],
[87033,68120],
[56673,79181],
[29191,66225],
[28547,73110],
[38779,36965],
[47650,28959],
[53542,63433],
[57326,77208],
[47397,74087],
[56974,91506],
[94380,89240],
[73519,64750],
[86072,66225],
[56637,86047],
[38835,56887],
[35194,31422],
[31030,91726],
[24289,83439],
[13380,96639],
[62485,19486],
[17925,98629],
[45322,58503],
[19858,70212],
[76974,70198],
[31209,42754],
[78649,19540],
[21269,30818],
[79879,74349],
[12287,43331],
[52902,97497],
[42256,72564],
[65683,98690],
[85852,12537],
[11177,58141],
[29845,56887],
[72128,60881],
[75118,64750],
[10694,88962],
[35398,14847],
[52585,77208],
[19847,96727],
[49904,78550],
[20209,67547],
[59782,73110],
[15208,96540],
[73305,24878],
[27291,28783],
[96959,56137],
[48917,10498],
[66195,51193],
[86018,14155],
[11183,87214],
[81471,20417],
[81075,36073],
[70524,56989],
[55350,73110],
[41092,32897],
[96875,98990],
[25671,71703],
[94256,93577],
[74818,28783],
[87291,66811],
[95610,88962],
[67630,73110],
[44931,27451],
[82786,60348],
[48823,74599],
[37348,27647],
[51403,21717],
[74065,66225],
[97472,10765],
[51171,39802],
[98631,26218],
[93577,38025],
[30551,61026],
[27245,26128],
[66225,32948],
[28109,69643],
[99919,52051],
[36190,39903],
[21731,70524],
[45178,41559],
[16489,60046],
[28422,49997],
[47181,28783],
[55334,45848],
[60355,10462],
[38054,58529],
[94168,43063],
[84267,93577],
[81139,66225],
[11979,69643],
[53210,92048],
[71293,14847],
[28632,29964],
[48453,70524],
[25528,88828],
[98629,30341],
[23981,42766],
[86550,64750],
[74837,73110],
[73970,95582],
[18388,70524],
[54128,27789],
[61782,97722],
[79062,28783],
[62747,40543],
[93244,88828],
[24097,64750],
[75472,52051],
[10332,36965],
[88748,10447],
[55654,97497],
[86183,18694],
[49296,40819],
[45688,61816],
[13853,87775],
[60828,10919],
[49362,13764],
[75734,30341],
[44383,30796],
[69130,89397],
[14394,60828],
[59796,60828],
[64841,62802],
[89637,24217],
[29765,91528],
[23664,14847],
[54698,42787],
[51718,14847],
[61760,47936],
[86551,52051],
[64750,19627],
[44194,41074],
[80148,51436],
[45040,64151],
[86619,68850],
[56887,26569],
[27207,88828],
[43005,11730],
[67425,56887],
[77208,71703],
[69953,86047],
[81173,70524],
[54060,20769],
[28961,39903],
[41721,79424],
[77450,60828],
[88239,72083],
[68765,28959],
[51750,71703],
[46092,69643],
[87649,22082],
[15083,36841],
[17705,90635],
[36459,80253],
[79316,77306],
[20938,58284],
[19290,79881],
[19402,28959],
[65440,77208],
[71703,87778],
[22049,28783],
[81029,94839],
[33070,16536],
[39672,78991],
[64972,90805],
[29826,60828],
[56454,22361],
[72748,73110],
[84099,98690],
[28580,52154],
[94868,67461],
[48509,53815],
[43905,60828],
[52804,56887],
[90981,36965],
[50826,28959],
[59759,39903],
[96729,61026],
[18065,86336],
[73110,98690],
[94751,60828],
[60339,13036],
[54603,95918],
[15533,41092],
[46194,21717],
[96083,97497],
[66050,88742],
[83300,52051],
[99478,69643],
[54133,41559],
[76181,52051],
[54994,27647],
[11240,60011],
[86495,24164],
[83944,69643],
[13427,17435],
[64112,28783],
[48326,86202],
[46457,77208],
[20953,28165],
[36595,35253],
[43417,89397],
[70015,14847],
[10555,31986],
[52788,47847],
[30414,76926],
[65544,16621],
[43561,48185],
[20248,32922],
[13017,86047],
[95482,77208],
[83191,88828],
[96807,75946],
[88225,54807],
[71793,67308],
[31137,85225],
[92329,69643],
[37724,68238],
[85629,41559],
[60011,27647],
[73545,77208],
[72353,47613],
[10324,42766],
[41710,66601],
[86047,70524],
[75902,21172],
[69007,10498],
[28649,60828],
[33474,36965],
[53043,86614],
[46770,30341],
[81528,83906],
[97188,12944],
[67655,87182],
[11391,93720],
[19579,56989],
[61763,98150],
[57694,66225],
[87231,84011],
[99204,10462],
[98673,19412],
[74616,39750],
[34466,32012],
[76876,93577],
[43464,56887],
[84649,60011],
[27522,11103],
[71002,48453],
[75736,51969],
[83595,64614],
[29606,80223],
[74920,68560],
[54988,66112],
[74107,98629],
[62825,53238],
[43473,56887],
[33340,17155],
[51207,69643],
[16790,88962],
[60249,73828],
[69492,57435],
[22009,43285],
[20158,93577],
[81424,30637],
[25576,92018],
[68989,98690],
[88258,86242],
[25607,27647],
[87096,72523],
[74941,21977],
[49680,79357],
[88728,33562],
[52149,24421],
[17869,86047],
[42485,10462],
[59373,98629],
[83521,16252],
[99438,12844],
[69743,21717],
[26973,29067],
[88483,56989],
[85468,24099],
[51804,14847],
[21717,70524],
[83992,56887],
[72526,84449],
[34325,69643],
[84671,77208],
[78922,42577],
[82942,14663],
[75146,95096],
[34756,75451],
[22720,71703],
[80055,37550],
[51370,24099],
[26465,86047],
[44919,21717],
[31829,48453],
[97103,10462],
[46742,41559],
[22511,88682],
[34385,42766],
[25198,67759],
[17684,65370],
[37931,54939],
[94817,56989],
[51436,98690],
[38382,23350],
[18076,59656],
[69587,26802],
[41886,28888],
[71572,88957],
[49411,28783],
[70055,70208],
[50040,21717],
[24733,98815],
[32343,36965],
[75319,86047],
[99792,57533],
[51677,88962],
[69872,53641],
[68258,35233],
[72704,20997],
[78327,63698],
[62435,56887],
[84014,77208],
[51255,53718]]


mini_in = [[3,4],
[4,3],
[2,5],
[1,3],
[3,9],
[3,3]]


''' ---------------------------- PART 1 ------------------------------------'''

my_in = actual_in

l_list = []

r_list=[]

for a in my_in:
    l_list+=[a[0]]
    r_list+=[a[1]]
    
l_list.sort()
r_list.sort()


tot=0
for i in range(len(l_list)):
    tot+= abs(l_list[i]-r_list[i])

print(tot)






''' ---------------------------- PART 2 ------------------------------------'''

my_in = actual_in

l_list = []

r_list=[]

for a in my_in:
    l_list+=[a[0]]
    r_list+=[a[1]]
    
tot = 0
for x in l_list:
    tot += x * r_list.count(x)

print(tot)



