import getCovid19Data

#data   august 19 2021
#cases=[1,1,1,1,1,2,2,4,7,10,10,10,15,15,22,28,32,41,52,66,73,78,93,99,110,124,133,149,163,230,248,267,304,333,368,391,412,438,446,463,479,494,508,520,541,548,575,582,609,619,630,632,641,658,663,668,672,673,677,677,682,688,696,704,707,710,717,721,725,729,733,737,740,741,750,784,796,809,845,859,870,878,886,891,902,911,931,954,961,1024,1086,1097,1114,1119,1140,1161,1168,1172,1191,1220,1233,1242,1256,1306,1312,1320,1331,1350,1368,1388,1402,1422,1442,1446,1464,1473,1489,1495,1510,1536,1587,1603,1622,1644,1662,1697,1719,1740,1745,1778,1788,1796,1830,1855,1873,1885,1907,1946,2012,2082,2168,2334,2419,2451,2542,2599,2700,2775,2859,2905,2980,3104,3260,3407,3582,3750,3882,4023,4205,4334,4555,4730,4885,5062,5271,5417,5672,5951,6223,6517,6812,7121,7413,7711,8045,8442,8881,9337,9758,10347,10952,11580,12191,12698,13155,13687,14248,14937,15613,16275,16870,17308,17777,18375,18963,19490,20011,20426,20826,21324,21877,22437,22983,23669,24310,24857,25449,26083,26768,27518,28297,29303,29987,30852,31792,32819,33962,35242,36254,37272,38377,39634,40882,42173,43494,44482,45657,46918,48377,49744,51170,52558,53568,54624,55869,57246,58745,60113,61284,62286,62944,64336,65577,67027,68479,69906,71390,72186,73995,75845,77778,79529,81228,82617,83697,85209,87097,89186,91328,93097,94236,95355,96907,98829,100703,102607,104267,105430,106446,107953,110037,111946,113655,115283,116476,117517,118705,122200,123982,125678,126944,127944,129455,131297,132817,134295,134495,137112,138096,139135,140409,142187,143705,145245,146520,147613,148877,150933,153049,154944,156570,158104,159286,160979,163225,165933,168069,169472,171226,172820,175118,177996,181503,183888,186408,189278,192139,195759,199925,204699,210139,215553,219296,222391,226948,231936,237132,243286,249158,252812,255956,260315,264647,269241,272461,276587,279597,282249,285754,289660,293157,296282,298913,301052,303072,305842,309162,312269,315340,317836,319917,321980,324866,328023,331159,334093,337138,339268,340868,343601,346080,348810,351065,353388,355056,356597,359320,362833,366302,369675,372775,375033,376921,380019,383482,386851,390053,393211,395588,397871,401810,405391,408909,411839,415362,418448,419953,423433,426977,430734,434322,436575,439543,441014,444865,448721,452281,455381,458338,461062,462339,465007,468400,471962,474925,477113,479501,480502,482798,485918,489428,491928,494633,496846,497854,499839,502299,504800,506808,508503,510403,511398,513006,515088,516600,518104,519615,520939,521581,522763,524241,525577,526578,527508,528208,528457,529205,530217,531234,531834,532269,532839,533141,533685,534388,534968,535181,535446,535753,535954,536554,537043,537437,537887,538218,538518,538668,538991,539271,539590,539888,540132,540277,540388,540630,540844,541009,541232,541423,541557,541628,541801,541940,542169,542375,542523,542604,542649,542819,542934,543099,543267,543371,543505,543551,543698,543865,544002,544165,544291,544454,544520,544705,544866,545016,545226,545363,545570,545671,545965,546336,546766,547170,547497,547811,547961,548455,548972,549427,550004,550492,550942,551157,551789,552328,552871,553615,554458,555302,555643,557145,558369,559473,560396,561380,562527,563124,564364,565896,567044,568505,570098,571650,572401,573959,576550,578367,579999,581497,583012,583718,584896,586585,588578,589597,590983,592156,592780,593929,595522,596854,597978,599298,600451,601226,602266,603288,604409,605521,606536,607400,608041,609189,610197,611097,611912,612713,613498,613982,614688,615532,616179,617036,617662,618278,618580,619232,619950,620552,621155,621735,622235,622440,622983,623609,624230,624743,625445,625974,626198,626926,627722,628241,628881,629561,630180,630382,630950,631642,632271,632781,633355,633909,634209,634669,635447,636147,636685,637312,637819,638054,638581,639332,639995,640675,641339,642024,642225,643047,643749,644391,645104,645805,646629,646869,647778,648782,649696,650655,651788,652735,654068,655174,656192,657367]#add confirmed cases here (cumulative)
#deaths=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,3,3,3,3,3,4,4,4,4,4,4,4,5,6,7,8,10,11,12,14,14,17,17,19,19,19,19,20,20,20,20,21,21,21,21,21,21,21,21,22,22,22,24,24,24,24,24,24,24,25,25,25,25,25,25,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,27,27,27,27,28,28,29,30,30,30,30,31,31,32,32,32,32,32,32,32,32,32,32,32,33,33,33,33,34,34,34,34,35,35,35,36,36,36,36,36,36,36,36,36,37,38,40,40,40,40,41,41,43,43,46,47,51,51,54,55,57,61,61,62,65,65,68,70,70,78,78,80,87,89,92,94,97,103,105,107,109,113,116,121,123,126,138,139,146,148,155,160,167,171,177,179,183,187,191,200,207,212,219,229,239,241,246,252,259,263,281,286,297,307,315,328,329,333,340,347,351,361,367,374,386,398,406,414,424,433,439,450,455,459,466,479,499,501,509,517,520,526,531,536,552,559,562,565,579,590,602,610,625,637,643,652,667,676,683,700,713,723,732,749,763,775,796,806,817,827,839,852,868,884,894,900,911,934,974,980,991,1004,1018,1033,1055,1067,1078,1078,1099,1115,1136,1156,1170,1182,1200,1200,1210,1223,1234,1248,1259,1270,1281,1294,1311,1333,1353,1367,1379,1394,1409,1430,1456,1468,1479,1489,1499,1512,1529,1550,1566,1570,1590,1606,1629,1705,1740,1781,1825,1866,1906,1959,2020,2084,2151,2208,2270,2320,2374,2477,2553,2621,2680,3031,3082,3145,3226,3315,3397,3495,3562,3616,3677,3737,3803,3866,3915,3961,3993,4037,4092,4152,4206,4257,4297,4340,4387,4446,4508,4560,4610,4652,4692,4743,4805,4866,4919,4971,5013,5046,5089,5134,5180,5230,5278,5334,5380,5422,5474,5536,5609,5664,5715,5757,5808,5850,5903,5964,6013,6058,6096,6136,6184,6234,6286,6346,6379,6409,6443,6479,6512,6549,6592,6630,6661,6703,6738,6778,6809,6854,6886,6925,6959,6995,7027,7057,7090,7118,7142,7171,7197,7224,7249,7278,7302,7324,7345,7368,7390,7415,7436,7460,7486,7507,7527,7549,7569,7586,7602,7620,7631,7641,7651,7658,7664,7670,7677,7684,7690,7697,7705,7711,7718,7723,7729,7735,7740,7747,7752,7758,7763,7769,7774,7780,7785,7790,7794,7798,7801,7804,7808,7811,7815,7819,7822,7825,7829,7832,7835,7839,7841,7843,7845,7848,7851,7854,7856,7859,7861,7863,7865,7867,7869,7871,7873,7875,7877,7879,7881,7882,7883,7884,7885,7886,7887,7888,7889,7890,7891,7892,7894,7895,7897,7900,7903,7906,7909,7912,7917,7921,7926,7932,7938,7943,7948,7952,7958,7962,7967,7972,7976,7982,7988,7993,7999,8004,8008,8011,8014,8019,8024,8031,8035,8040,8044,8048,8053,8061,8070,8079,8089,8101,8114,8129,8144,8157,8169,8181,8192,8202,8210,8218,8224,8228,8232,8236,8240,8246,8253,8260,8268,8277,8286,8296,8306,8316,8325,8333,8341,8348,8356,8363,8370,8375,8379,8382,8385,8389,8394,8400,8406,8413,8419,8425,8430,8434,8438,8441,8445,8449,8453,8459,8465,8472,8480,8488,8495,8502,8509,8515,8522,8528,8534,8540,8546,8551,8556,8561,8566,8571,8577,8582,8596,8606,8616,8625]#add confirmed death here (cumulative)
#recoveries=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,3,3,3,3,8,8,8,8,20,23,23,30,30,32,32,43,44,54,54,54,60,64,64,67,67,67,67,67,80,80,85,85,99,100,102,108,140,140,143,145,145,145,150,150,150,150,150,200,200,200,220,220,234,234,234,234,236,236,246,247,247,251,251,251,663,663,667,688,688,689,692,699,705,708,712,715,719,724,731,768,768,768,768,768,768,845,853,868,868,875,889,907,944,960,1006,1068,1077,1098,1103,1144,1144,1153,1153,1170,1183,1223,1242,1292,1304,1311,1311,1348,1368,1368,1402,1402,1420,1423,1452,1455,1485,1485,1485,1515,1562,1577,1607,1619,1666,1671,1692,1709,1710,1753,1753,1761,1761,1795,1837,1837,1880,1974,2042,2043,2127,2290,2377,2407,2496,2551,2650,2724,2809,2852,2928,3040,3204,3346,3625,3704,3723,3955,4133,4260,4484,4693,4811,4988,5195,5338,5592,5868,6139,6430,6722,7024,7312,7312,7936,8334,8765,9216,9634,10217,10739,11440,12047,12507,12878,13527,14112,14778,15434,16089,16676,17110,17565,18103,18739,19259,19782,20243,20490,21120,21760,22407,22719,23501,23941,24581,25164,25994,26468,27197,28062,28855,29498,30470,31409,32412,33438,34803,35545,36797,37787,39123,40352,41624,42904,43885,43885,45032,45820,45820,46602,46602,51728,53360,54869,55706,57693,58538,60416,61263,62395,62528,63404,64685,66135,67667,69079,70555,72152,74008,74950,76774,83034,83034,83034,84142,86019,86019,90229,90229,93100,94042,95737,97647,98584,101334,103057,104207,104207,106712,106712,110535,112333,113948,115124,116143,116143,118947,118947,122547,124234,125473,126460,127959,127959,131000,132768,134367,135596,136566,137582,138839,140569,142239,143716,144857,145873,147746,147746,151080,153038,154608,156084,157202,158822,162007,164348,165729,168142,168749,170067,172497,175397,178472,180877,180877,186052,188824,192324,194430,201137,206523,211879,215359,217578,222078,224380,226658,239293,245093,248720,250994,256109,260390,264894,268071,272200,275151,277741,281194,285050,288505,291590,294170,296247,298206,300923,304191,307256,310294,312747,314783,316800,319629,322738,325818,328706,331570,333648,335325,337975,340399,343078,343078,347563,349206,350694,353356,356820,360244,363441,366639,368849,370687,373733,377136,380472,380472,386768,389109,391359,395261,398799,402279,402279,408659,411710,413175,416624,420123,423848,423848,429616,432548,433987,437808,441631,445163,445163,451167,453865,455115,457758,461122,464660,464660,464660,472133,473122,475383,478482,481968,481968,487126,489319,490305,492270,492270,497198,497198,500872,502762,503747,505348,507424,508930,508930,511931,513249,513884,515058,516530,517859,517859,519779,520473,520717,521458,522465,523476,523476,524500,525065,525065,525900,526598,527174,527174,527645,527949,528146,528743,529228,529618,529618,530393,530689,530836,531156,531432,531749,531749,532287,532429,532537,532776,532776,533150,533150,533560,533692,533761,533932,534069,534296,534296,534646,534725,534768,534937,535051,535216,535216,535485,535485,535663,535663,535663,536111,536111,536397,536559,536623,536805,536963,537111,537111,537451,537653,537653,538039,538434,538828,538828,538828,539859,540003,540493,541005,541455,541455,542510,542954,543164,543790,544324,544863,544863,546444,547283,547624,549114,550334,551433,551433,553332,554474,555063,556294,557817,558955,558955,561984,563521,564257,564257,568381,570186,570186,573295,574802,575500,576672,578357,580346,580346,582743,583910,584527,585669,587254,588577,588577,591002,592145,592910,593941,594955,596068,596068,598180,599037,599671,600814,601818,602715,602715,604324,605104,605582,606282,607119,607760,607760,609232,609844,610142,610142,611505,612103,612103,613276,613770,613968,614503,615121,615735,615735,616936,617459,617676,618398,619188,619701,619701,621010,621624,621821,622384,623071,623694,623694,625313,625603,626053,626822]#add confirmed recoveries here (cumulative)
#get uptodate data
upToDateData=getCovid19Data.GetCovid19DataLeb()
cases=upToDateData["total cases"]
for i in range (len(cases)):
    if (cases[i]!=0):
        break
cases=cases[i:]
deaths=upToDateData["total deaths"]
deaths=deaths[i:]
tempactivecases=upToDateData["active cases"]
tempactivecases=tempactivecases[i:]
recoveries=[(cases[i]-tempactivecases[i]-deaths[i]) for i in range (len(cases))]


Pcr=[]#add number of cumulative PCR tests here
PCRPositivityRate=[]#add number of daily positivity rate of PCR test here
Fvaccinated=[]#add number of fully vacinated peaple here
Pvaccinated=[]#add number of first dose onlu vacinated peaple here
population= 6809584#total population    

#imports
import matplotlib.pyplot as plt
import numpy as np
import math
#from numpy import log as ln



#needed values
l=len(cases)
day=[1+i for i in range (l) ]
aproxy=(cases[l-1])**(1/(l-1))








def trilleme(x):
#    if (abs(x)>0.1):
    x=x*1000000
    a=x-int(x)
    if (abs(a)>=0.5):
        x=int(x)+1
    else:
        x=int(x)
    x=x/1000000
    return x



#converts any float to a float with 3 numbers after the .
#if number given > than 0.1
def milleme(x):
#    if (abs(x)>0.1):
    x=x*1000
    a=x-int(x)
    if (abs(a)>=0.5):
        x=int(x)+1
    else:
        x=int(x)
    x=x/1000
    return x


#same as milleme but bypasses that the number is bigger than 0.1
def millemebuypass(x):
        x=x*1000
        a=x-int(x)
        if (abs(a)>=0.5):
            x=int(x)+1
        else:
            x=int(x)
        x=x/1000
        return x


#round any nouber to the closeset integer
def rond(x):
    if(abs(x)>0.1):
        a=x-int(x)
        if (a>=0.5):
            x=int(x)+1
        else:
            x=int(x)
    return(x)






#daily cases list
newcases=[0]*l
newcases[0]=1
for i in range(1,l):
    newcases[i]=cases[i]-cases[i-1]


#active cases list
activecases=[0]*l
for i in range (l):
    activecases[i]=cases[i]-recoveries[i]-deaths[i]


#daily recoveries list
newrecoveries=[0]*l
newrecoveries[0]=0
for i in range (1,l):
    newrecoveries[i]=recoveries[i]-recoveries[i-1]


#daily deaths
newdeaths=[0]*l
newdeaths[0]=0
for i in range (1,l):
    newdeaths[i]=deaths[i]-deaths[i-1]

    
#daily growth
dailygrowth=newcases[l-1]/cases[l-2]*100
dailygrowth=milleme(dailygrowth)


#active cases daily growth
activegrowth=(activecases[l-1]-activecases[l-2])/activecases[l-2]*100
activegrowth=milleme(activegrowth)


#death rate
deathrate=(deaths[l-1]/cases[l-1])*100
deathrate=milleme(deathrate)


#recovery rate
recoveryrate=(recoveries[l-1]/cases[l-1])*100
recoveryrate=milleme(recoveryrate)


#population infected
popinf=milleme(cases[l-1]/population *100)
curpopinf=milleme(activecases[l-1]/population *100)
popinfthisweek=millemebuypass((cases[l-1]-cases[l-8])/population *100)
popinfthismonth=millemebuypass((cases[l-1]-cases[l-31])/population *100)
thisweekpopinfpercperpopinf=milleme((cases[l-1]-cases[l-8])/cases[l-1] *100)
thismonthpopinfpercperpopinf=milleme((cases[l-1]-cases[l-31])/cases[l-1] *100)
thisdaypopinfpercperpopinf=millemebuypass((newcases[l-1])/cases[l-1] *100)
riskperweek=millemebuypass((cases[l-1]-cases[l-8])/(population-cases[l-1]-deaths[l-1]) *100)
riskpermonth=millemebuypass((cases[l-1]-cases[l-31])/(population-cases[l-1]-deaths[l-1]) *100)
riskperday=millemebuypass((newcases[l-1]+newcases[l-2])/(2*(population-cases[l-1]-deaths[l-1])) *100)


#daily change in active cases
changeactivecases=[0]*l
changeactivecases[0]=1
for i in range (1,l):
    changeactivecases[i]=activecases[i]-activecases[i-1]


#last 14 days cumulative
lcases=[cases[i]for i in range (l-14,l)]
lrecoveries=[recoveries[i]for i in range (l-14,l)]
ldeaths=[deaths[i]for i in range (l-14,l)]
lactivecases=[activecases[i]for i in range (l-14,l)]
lday=[i+1 for i in range (l-14,l)]


#last 14 days daily
lnewcases=[newcases[i]for i in range (l-14,l)]
lnewrecoveries=[newrecoveries[i]for i in range (l-14,l)]
lnewdeaths=[newdeaths[i]for i in range (l-14,l)]









# #expectation for tomorrow
# newcasessort=[newcases[l-5],newcases[l-4],newcases[l-3],newcases[l-2],newcases[l-1]]
# newcasessort.sort()
# exptomd=rond(((newcasessort[0]*0.7+newcasessort[1]+newcasessort[2]*2 +newcasessort[3]+newcasessort[4]*0.7)+newcases[l-1]*1.3+newcases[l-2]*1+newcases[l-3]*0.7+newcases[l-4]*0.5+newcases[l-5]*0.4)/9.3)
# exptom=exptomd +cases[l-1]


# #expectation for tomorrow.2
# casesnextdaymid=cases[l-1]+(newcases[l-1]+newcases[l-2])/2
# x=aproxy**(l)
# if ((cases[l-1]-cases[l-2])>0):
#     casesnextdaymax=(x+casesnextdaymid)/2
# if (casesnextdaymid-int(casesnextdaymid)<0.5):
#     casesnextdaymid=int(casesnextdaymid)
# else:
#     casesnextdaymid=int(casesnextdaymid)+1
# if (casesnextdaymax-int(casesnextdaymax)<0.5):
#     casesnextdaymax=int(casesnextdaymax)
# else:
#     casesnextdaymax=int(casesnextdaymax)+1






#averages
avrdeathlastweek=0
avrcaseslastweek=0    
for i in range (l-8,l):
    avrdeathlastweek=avrdeathlastweek+newdeaths[i]
    avrcaseslastweek=avrcaseslastweek+newcases[i]
avrdeathlastweek=rond(avrdeathlastweek/8)
avrcaseslastweek=rond(avrcaseslastweek/8)


#up or down from last  week
markerd=0
fatalityweekold=deaths[l-8]/cases[l-8] *100
if (fatalityweekold<deathrate):
    markerd=1
elif(fatalityweekold>deathrate):
    markerd=-1

markerr=0
recoveryweekold=recoveries[l-8]/cases[l-8] *100
if (recoveryweekold<recoveryrate):
    markerr=1
elif(recoveryweekold>recoveryrate):
    markerr=-1

markera=0
activecasesweekold=activecases[l-8]
if (activecases[l-1]>activecasesweekold):
    markera=1
elif(activecases[l-1]<activecasesweekold):
    markera=-1

#Active cases % from cases
CurentActiveCases=milleme(activecases[l-1]/cases[l-1] *100)










#Lines Of Best Fit

#Linear line of best fit
#y=ax+b
def LinearLineOfBestFit(L,D):
    try:
        l=len(L)
        AverageOfL=0
        AverageOfD=0
        for i in range (l):
            AverageOfL=AverageOfL+L[i]
            AverageOfD=AverageOfD+D[i]
        AverageOfL=AverageOfL/l
        AverageOfD=AverageOfD/l
        
        
        ANumerator=0
        ADenomenator=0
        for i in range (l):
            ANumerator=ANumerator+((L[i]-AverageOfL)*(D[i]-AverageOfD))
            ADenomenator=ADenomenator+(D[i]-AverageOfD)**2
        a=ANumerator/ADenomenator
        b=AverageOfL-a*AverageOfD
        return ([a,b])
    except ZeroDivisionError:
        print("Line estimate for one point is not definned")
    

#y=Ar^x  (y=L and x=D)
def ExponentialLineOfBestFit(L,D):
    C=[np.log10(L[i]) for i in range (len(L))]
    Tr=LinearLineOfBestFit(C,D)
    r=10**Tr[0]
    A=10**Tr[1]
    return([A,r])

#Quadratic Regression
#y=ax^2 + bx + c
def QuadraticLineOfBestFit(L,D):
    n=len(L)
    sumX=0
    sumY=0
    sumX2=0
    sumX3=0
    sumX4=0
    sumXY=0
    sumX2Y=0
    for i in range (n):
        sumX=sumX+D[i]
        sumY=sumY+L[i]
        sumX2=sumX2+(D[i])**2
        sumX3=sumX3+(D[i])**3
        sumX4=sumX4+(D[i])**4
        sumXY=sumXY+L[i]*D[i]
        sumX2Y=sumX2Y+((D[i])**2)*L[i]
    a=(((sumX2Y-(sumX2*sumY)/n)*((sumX2)-((sumX)**2)/n))-(((sumXY)-(sumX*sumY)/n)*((sumX3-(sumX2*sumX)/n))))/((((sumX2)-((sumX)**2)/n)*(sumX4-((sumX2)**2)/n))-((sumX3-(sumX2*sumX)/n)**2))
    b=((((sumXY)-(sumX*sumY)/n)*(sumX4-((sumX2)**2)/n))-((sumX2Y-(sumX2*sumY)/n)*(sumX3-(sumX2*sumX)/n)))/((((sumX2)-((sumX)**2)/n)*(sumX4-((sumX2)**2)/n))-((sumX3-(sumX2*sumX)/n)**2))
    c=(sumY/n)-(b*sumX/n)-(a*sumX2/n)
    return([a,b,c])



def EveryXLineOfBestFit(L,D,X):
    l=len(L)
    tot=[0]*l
    for i in range (0,l-X+1,X):
        x=[j for j in range (i,i+X)]
        y=[L[j] for j in range (i,i+X)]
        ITlinLineOfBestFit=LinearLineOfBestFit(y,x)
        for j in range (i,i+X):
            tot[j]=ITlinLineOfBestFit[0]*D[j]+ITlinLineOfBestFit[1] 
    remL=math.ceil((l/X - int(l/X))*X)
    if (remL>1):
        tempY=[L[i] for i in range (l-1-remL,l)]
        tempX=[D[i] for i in range (l-1-remL,l)]
        LastITlinLineOfBestFit=LinearLineOfBestFit(tempY,tempX)
        for i in range (l-1,l-2-remL,-1):
            tot[i]=LastITlinLineOfBestFit[0]*D[i]+LastITlinLineOfBestFit[1]    
    elif(remL==1):
        tot[l-1]=L[l-1]
    return(tot)











#Linear Line of best fit for cases
linLineOfBestFit=LinearLineOfBestFit(cases,day)
linLineOFBestFitCases=[(linLineOfBestFit[0]*day[i]+linLineOfBestFit[1]) for i in range (l)]

#Exponential Line of best fit for cases
ExpoLineOfBestFit=ExponentialLineOfBestFit(cases,day)
ExpoLineOfBestFitCases=[ExpoLineOfBestFit[0]*(ExpoLineOfBestFit[1]**day[i]) for i in range (l)]

#Quadratic Line of best fir for cases
QuadLineOfBestFit=QuadraticLineOfBestFit(cases,day)
QuadLineOfBestFitCases=[(QuadLineOfBestFit[0]*day[i]**2+QuadLineOfBestFit[1]*day[i]+QuadLineOfBestFit[2]) for i in range (l)]

#Libear line of best fit for daily cases interative
a=15
totCases=EveryXLineOfBestFit(newcases,day,a)
totRecoveries=EveryXLineOfBestFit(newrecoveries,day,a)
totDeaths=EveryXLineOfBestFit(newdeaths,day,a)
totActivecasechange=EveryXLineOfBestFit(changeactivecases,day,a)






#calculating average error of expectation
expectedTomArray=[0]*(l-3)
for p in range (3,l):
    last7dayscases=[cases[i] for i in range (p-3,p+1)]
    last7days=[i+1 for i in range (p-3,p+1)]
    # linexpectationcoef=LinearLineOfBestFit(last7dayscases,last7days)
    # linexpectation=[linexpectationcoef[0]*last7days[i] +linexpectationcoef[1] for i in range (len(last7dayscases))]
    # LinVar=0
    # for i in range (len(last7dayscases)):
    #     LinVar=LinVar+(last7dayscases[i]-linexpectation[i])**2

    quadraticxpectationcoef=QuadraticLineOfBestFit(last7dayscases,last7days)
    quadraticxpectation=[((quadraticxpectationcoef[0]*(last7days[i])**2)+quadraticxpectationcoef[1]*last7days[i]+quadraticxpectationcoef[2]) for i in range (len(last7dayscases))]
    #QuadVar=0
    #for i in range (len(last7dayscases)):
        #QuadVar=QuadVar+(last7dayscases[i]-quadraticxpectation[i])**2
    using="Quadratic"
    expectedTom=int(quadraticxpectationcoef[0]*((day[p]+1)**2)+quadraticxpectationcoef[1]*(day[p]+1)+quadraticxpectationcoef[2])

    if (expectedTom<=cases[p]):
        using="Linear Small"
        lastdayscases=[cases[i] for i in range (p-2,p+1)]
        lastdays=[i+1 for i in range (p-2,p+1)]
        LinregOflastdays=LinearLineOfBestFit(lastdayscases,lastdays)
        expectedTom=int(LinregOflastdays[0]*(day[p-1]+1) +LinregOflastdays[1])

    if (expectedTom<cases[p]):
        using="Last Resort"
        expectedTom=cases[p]+newcases[p]
    expectedTomArray[p-3]=expectedTom

  



  
#compare qudratic line of best fit with actuale cases
# expectedTomGraph=[(int(quadraticxpectationcoef[0]*((day[l-i])**2)+quadraticxpectationcoef[1]*(day[l-i])+quadraticxpectationcoef[2])) for i in range (4,0,-1)]    
# DayGraphExpected=[day[i] for i in range (l-4,l)]  
# casesEstimate=[cases[i] for i in range (l-4,l)]    


#More estimation error calculation with + and - 
error=0
ErrorArray=[0]*(l-4)
Overerr=0
OvererrCounter=0
Undererr=0
UndererrCounter=0
equal=0
for i in range (l-4):
    CurErr=abs(((expectedTomArray[i]-cases[i+4])/cases[i+4]) *100)
    error=CurErr+error
    #ErrorArray[i]=CurErr
    if(expectedTomArray[i]-cases[i+4] >0):
        OvererrCounter=OvererrCounter+1
        Overerr=Overerr+CurErr
    elif(expectedTomArray[i]-cases[i+4] <0):
        UndererrCounter=UndererrCounter+1
        Undererr=Undererr-CurErr
    else:
        equal=equal+1
error=error/(l-4)
if (OvererrCounter>0):
    Overerr=Overerr/OvererrCounter
if (UndererrCounter>0):
    Undererr=Undererr/UndererrCounter

#what % prediction were within margin of error
withinMargin=0
for i in range(l-4):
    if(abs(expectedTomArray[i]-cases[i+4])<(error/100 *cases[i+4])):
        withinMargin=withinMargin+1
withinMargin=withinMargin/(l-4) *100





#estimation error calculation with + and -
RecentError=0
RecentErrorPos=0
RecentErrorPosCount=0
RecentErrorNeg=0
RecentErrorNegCount=0
for i in range (l-12,l-4):
    RecentError=abs(((expectedTomArray[i]-cases[i+4])/cases[i+4]) *100)+RecentError
    if (expectedTomArray[i]>cases[i+4]):
        RecentErrorPos=RecentErrorPos+(((expectedTomArray[i]-cases[i+4])/cases[i+4]) *100)
        RecentErrorPosCount=RecentErrorPosCount+1
    elif (expectedTomArray[i]<cases[i+4]):
        RecentErrorNeg=RecentErrorNeg+(((expectedTomArray[i]-cases[i+4])/cases[i+4]) *100)
        RecentErrorNegCount=RecentErrorNegCount+1
RecentError=RecentError/7
if (RecentErrorPosCount>0):
    RecentErrorPos=RecentErrorPos/RecentErrorPosCount
if (RecentErrorNegCount>0):
    RecentErrorNeg=RecentErrorNeg/RecentErrorNegCount








#for graphing purpuseonly to compare cases vs estimated cases
lo=l-30
QuadEstOfLastDays=[(expectedTomArray[i]-cases[i+3]) for i in range (lo,l-4)]
CasesOfLastDays=[newcases[i+4] for i in range (lo,l-4)]
dayy=[i+1 for i in range (lo+4,l)]


# QuadEstOfDays=[(expectedTomArray[i]) for i in range (0,l-4)]
# CasesDays=[cases[i+3] for i in range (0,l-4)]
# dayDs=[i+1 for i in range (4,l)]


#to show estimated new cases graphically
lastDay=[l,l+1]
LastDayEstimatedLine=[newcases[l-1],expectedTom-cases[l-1]]


#better error rate
#newexpectedTomArray=[expectedTomArray[i]-( error/100 *cases[i+4]) for i in range (l-4)]


# for i in range (0,4):
#     QuadEstOfLast4Days[i]=int(quadraticxpectationcoef[0]*((day[l-(i+4)])**2)+quadraticxpectationcoef[1]*(day[l-(i+4)])+quadraticxpectationcoef[2])

# for i in range (30):
#     print("Day:",day[i+4],"Actuale:",cases[i+4],"Expected:",expectedTomArray[i],"Error:",ErrorArray[i])









#no longer needed cause calculated in the average error of ecpectation
# #expected for tommorow using line of best fit choosing between linear or quadratique based on last 4 days
# last7dayscases=[cases[i] for i in range (l-4,l)]
# last7days=[i+1 for i in range (l-4,l)]
# linexpectationcoef=LinearLineOfBestFit(last7dayscases,last7days)
# linexpectation=[linexpectationcoef[0]*last7days[i] +linexpectationcoef[1] for i in range (len(last7dayscases))]
# LinVar=0
# for i in range (len(last7dayscases)):
#     LinVar=LinVar+(last7dayscases[i]-linexpectation[i])**2

# quadraticxpectationcoef=QuadraticLineOfBestFit(last7dayscases,last7days)
# quadraticxpectation=[((quadraticxpectationcoef[0]*(last7days[i])**2)+quadraticxpectationcoef[1]*last7days[i]+quadraticxpectationcoef[2]) for i in range (len(last7dayscases))]
# QuadVar=0
# for i in range (len(last7dayscases)):
#     QuadVar=QuadVar+(last7dayscases[i]-quadraticxpectation[i])**2

# if(LinVar<QuadVar):#using linear
#     using="Linear"
#     expectedTom=int (linexpectationcoef[0]*(day[l-1]+1)+linexpectationcoef[1])
# else:#using quadratic
#     using="Quadratic"
#     expectedTom=int(quadraticxpectationcoef[0]*((day[l-1]+1)**2)+quadraticxpectationcoef[1]*(day[l-1]+1)+quadraticxpectationcoef[2])

# if (expectedTom<=cases[l-1]):
#     using="Linear Small"
#     lastdayscases=[cases[i] for i in range (l-3,l)]
#     lastdays=[i+1 for i in range (l-3,l)]
#     LinregOflastdays=LinearLineOfBestFit(lastdayscases,lastdays)
#     expectedTom=int(LinregOflastdays[0]*(day[l-1]+1) +LinregOflastdays[1])

# if (expectedTom<cases[l-1]):
#     using="Last Resort"
#     expectedTom=cases[l-1]+newcases[l-1]









#expectation with corected variable(experimental)
#y=Ae^(B*t)
#oldb=1
#newb=0.2
#binn=0
#test=0
#while (abs(newb-oldb)>0.0001):
#    if(binn==0):
#        a1=cases[l-5]/(2.718)**((l-5)*newb)
#        a2=cases[l-4]/(2.718)**(newb*(l-4+1))
#        a3=cases[l-3]/(2.718)**(newb*(l-3+2))
#        a4=cases[l-2]/(2.718)**(newb*(l-2+3))
#        a5=cases[l-1]/(2.718)**(newb*(l-1+4))
#        at=(a1+a2+a3+a4+a5)/5
#        binn=1
#    else:
#        b1=(ln((cases[l-5])/at))/(l-5)
#        b2=ln((cases[l-4])/at)/(l-4+1)
#        b3=ln((cases[l-3])/at)/(l-3+2)
#        b4=ln((cases[l-2])/at)/(l-2+3)
#        b5=ln((cases[l-1])/at)/(l-1+4)
#        oldb=newb
#        newb=(b1+b2+b3+b4+b5)/5
#        binn=0
#        
#exptomcorr=at*2.718**(newb*(l))
#print(at)
#print(newb)
#print(exptomcorr)
#print(at*2.718**(newb*(l-1)))
    









#plots
plt.figure(1)
plt.plot(day,cases,"g")
plt.plot(day,deaths,"r")
plt.plot(day,recoveries,"b")
plt.plot(day,activecases,"gold")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Cumulative Curves')

plt.figure(2)
plt.plot(day,newcases,"g")
plt.plot(day,totCases,"black")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Daily Cases')

plt.figure(3)
plt.plot(day,newrecoveries,"b")
plt.plot(day,totRecoveries,"black")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Daily Recoveries')

plt.figure(4)
plt.plot(day,newdeaths,"r")
plt.plot(day,totDeaths,"black")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Daily Deaths')

plt.figure(5)
zero=[0]*l
plt.plot(day,zero,"brown")
plt.plot(day, changeactivecases,"gold")
plt.plot(day,totActivecasechange,"black")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Daily Changes In Active Cases')

#pie chart
plt.figure(6)
p = np.array([deathrate,recoveryrate,(100-recoveryrate-deathrate)])
mylabels=["Death","Recovery","Active"]
mycolors=["red","b","gold"]
myexplode=[0.1,0.4,0.1]
plt.pie(p, labels = mylabels, colors = mycolors, shadow = True, explode=myexplode,startangle=0,autopct='%1.1f%%',)
plt.show()

plt.figure(7)
plt.plot(lday,lnewcases,"g")
plt.plot(lday,lnewdeaths,"r")
plt.plot(lday,lnewrecoveries,"b")
plt.plot(lastDay,LastDayEstimatedLine,"black")
plt.plot()
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Daily Curves of last 14 days + Estimate')

plt.figure(8)
plt.plot(dayy,CasesOfLastDays,"g")
plt.plot(dayy,QuadEstOfLastDays,"black")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Cases and Estimated Cases')

# plt.figure(9)
# plt.plot(DayGraphExpected,casesEstimate,"g")
# plt.plot(DayGraphExpected,expectedTomGraph,"black")
# plt.xlabel('Days')
# plt.ylabel('Human numbers')
# plt.title('Cases and Estimated Cases')


# plt.figure()
# plt.plot(dayDs,CasesDays,"g")
# plt.plot(dayDs,QuadEstOfDays,"black")
# plt.xlabel('Days')
# plt.ylabel('Human numbers')
# plt.title('Cumulative Cases and Cumulative Estimated Cases')


plt.figure(10)
plt.plot(lday,lcases,"g")
plt.plot(lday,ldeaths,"r")
plt.plot(lday,lrecoveries,"b")
plt.plot(lday,lactivecases,"gold")
plt.xlabel('Days')
plt.ylabel('Human numbers')
plt.title('Cumulative Curves of last 14 days')

# plt.figure(10)
# plt.plot(day,cases,"g")
# plt.plot(day,linLineOFBestFitCases,"turquoise")
# #plt.plot(day,ExpoLineOfBestFitCases,"brown")
# plt.plot(day,QuadLineOfBestFitCases,"grey")
# plt.xlabel('Days')
# plt.ylabel('Human numbers')
# plt.title('Cumulative cases Curve AND lines of best fit')



#prints
print()
print("Day 0 of first confirmed Covid-19 case in Lebanon was on 21/02/2020")
print()
print("                                         Comaprison to last week:")
print("Cumulative numbers:")
print("     Day",l)
print("     Green curve is for cases.         Curently=", cases[l-1],"up by",cases[l-1]-cases[l-8])
print("     Red   curve is for deaths.        Curently=",deaths[l-1],"up by",deaths[l-1]-deaths[l-8])
print("     Bleu  curve is for recoveries.    Curently=",recoveries[l-1],"up by",recoveries[l-1]-recoveries[l-8])
if (markera==1):
    print("     Gold  curve is for active cases.  Curently=",activecases[l-1],"up by",activecases[l-1]-activecasesweekold)
elif(markera==-1):
        print("     Gold  curve is for active cases.  Curently=",activecases[l-1],"down by",-activecases[l-1]+activecasesweekold)
else:
        print("     Gold  curve is for active cases.  Curently=",activecases[l-1],"same as last week")
print()
print()

print("Daily numbers:")
print("     New cases       =",newcases[l-1])
print("     New recoveries  =",newrecoveries[l-1])
print("     New deaths      =",newdeaths[l-1])
print("     New active cases=",changeactivecases[l-1])
print()
print()

print("Statistics:")
print("     Cases daily growth       =",dailygrowth,"%")
if (markerd ==1):
    print("     Fatality                 =",deathrate,"% up by",millemebuypass(-fatalityweekold+deathrate),"%")
elif (markerd ==-1):
    print("     Fatality                 =",deathrate,"% down by",millemebuypass(fatalityweekold-deathrate),"%")
else:
    print("     Fatality                 =",deathrate,"% same as last week")
if(markerr==1):
    print("     Recovery                 =",recoveryrate,"% up by",millemebuypass(-recoveryweekold+recoveryrate),"%")
elif(markerr==-1):
    print("     Recovery                 =",recoveryrate,"% down by",millemebuypass(recoveryweekold-recoveryrate),"%")
else:
    print("     Recovery                 =",recoveryrate,"% same as last week")
print("     Active cases             =",CurentActiveCases,"%")
print("     Active cases daily growth=",activegrowth,"%")
print()
print()

#print("Expected for tomorrow:")
#if(exptom<=casesnextdaymid):
#    print("     Cumulative cases between",exptom,"and",casesnextdaymax)
#    print("     New cases between       ",exptomd,"and",casesnextdaymax-cases[l-1])  
#else:
#    print("     Cumulative cases between",casesnextdaymid,"and",casesnextdaymax)
#    print("     New cases between       ",casesnextdaymid-cases[l-1],"  and",casesnextdaymax-cases[l-1])
#print("     Worst case senario (exponential rout)",int(x), "so +",int(x)-cases[l-1])
#print()
#print()

print("Expected for tomorrow:","[",using,"]")
#print("    ",expectedTom,"cases")
print("    ",expectedTom-cases[l-1],"new cases","with Margins (","-",int((RecentErrorPos/100)*cases[l-1]),"; +",int(-(RecentErrorNeg/100)*cases[l-1]),")")#"+-",int((RecentError/100)*cases[l-1]))
print("     Average error for expectation model from day 4 till day",l-1,"=",milleme(error),"%")
print("     More presision about average error:")
print("         Over  Estimation=",milleme(Overerr),"%")
print("         Under Estimation=",abs(milleme(Undererr)),"%")
print("     Predictions within margin of error=",milleme(withinMargin),"%")
print()
print()


print("More info:")
print("     Total population infected  =",popinf,"%")
print("     Current population infected=",curpopinf,"%")
print("     Population infected last 7 days=",popinfthisweek,"%")
print("     Population infected last 30 days=",popinfthismonth,"%")
print("     Today recorded",thisdaypopinfpercperpopinf,"% of total infections")
print("     Last 7 days recorded",thisweekpopinfpercperpopinf,"% of total infections")
print("     Last 30 days recorded",thismonthpopinfpercperpopinf,"% of total infections")
print("     Risck of infection /Day=",riskperday,"%")
print("     Risck of infection /Week=",riskperweek,"%")
print("     Risck of infection /Month=",riskpermonth,"%")
print("     Average cases per day last 7 days =",avrcaseslastweek)
print("     Average deaths per day last 7 days =",avrdeathlastweek)
print("     Most cases in one day      =",max(newcases))
print("     Most recoveries in one day =",max(newrecoveries))
print("     Most deaths in one day     =",max(newdeaths))
print("     Most active cases hit      =",max(activecases))
print("     Vaccination began",l-1-357,"days ago. On 14/02/2021")
print()
print()

print("Notes:")
print("     Vaccinations are not taken into account in Risck calculations")

# print("More info about Graphs:")
# print("     Ligh Bleu line is linear line of best fit")
# print("     Gray line is quadratic line of best fit")

