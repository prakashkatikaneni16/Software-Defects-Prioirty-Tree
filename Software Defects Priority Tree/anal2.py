#pip3 install decision-tree-id3
#pip3 install graphviz
import pandas as pd
import math
col_names = ['ttype','pfuncaffec','workfaffec','severity','custsaffec','priority']
# load dataset
bugdtls = pd.read_csv("data121.csv", header=None, names=col_names)
#split dataset in features and target variable
feature_cols = ['ttype','pfuncaffec','workfaffec','severity','custsaffec']

#tpcnt stands for total priority count
tpcnt1 = len(bugdtls[bugdtls['priority'] == 1])
tpcnt2 = len(bugdtls[bugdtls['priority'] == 2])
tpcnt3 = len(bugdtls[bugdtls['priority'] == 3])
tpcnt4 = len(bugdtls[bugdtls['priority'] == 4])
tpcnt = tpcnt1 + tpcnt2 + tpcnt3 + tpcnt4
infopr = (-1*float(tpcnt1)/float(tpcnt)*math.log(float(tpcnt1)/float(tpcnt),2))- (float(tpcnt2)/float(tpcnt)*math.log(float(tpcnt2)/float(tpcnt),2)) \
- (float(tpcnt3)/float(tpcnt)*math.log(float(tpcnt3)/float(tpcnt),2)) - (float(tpcnt4)/float(tpcnt)*math.log(float(tpcnt4)/float(tpcnt),2))
#print('Info of Priority attribute is:',infopr) 
#nut stands for number of Unit test bugs,nit stands for number of integration test bugs
nut = len(bugdtls[bugdtls['ttype'] == 0])
nit = len(bugdtls[bugdtls['ttype'] == 1])
nst = len(bugdtls[bugdtls['ttype'] == 2])
nat = len(bugdtls[bugdtls['ttype'] == 3])
#tnor stands for total no.of rows
tnor = nut + nit + nst + nat 
print("No.of Unit,Integration,System & Acceptance Test Bugs Are:",nut,nit,nst,nat)
#cutbp1 stands for count of unit test bugs with priority '1'
cutbp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.ttype == 0)])
cutbp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.ttype == 0)])
cutbp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.ttype == 0)])
cutbp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.ttype == 0)])
print("No.of Unit test bugs with different priorities are:",cutbp1,cutbp2,cutbp3,cutbp4)
#citbp1 stands for count of Int. test bugs with priority '1'
citbp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.ttype == 1)])
citbp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.ttype == 1)])
citbp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.ttype == 1)])
citbp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.ttype == 1)])
print("No.of Int. test bugs with different priorities are:",citbp1,citbp2,citbp3,citbp4)
#cstbp1 stands for count of system test bugs with priority '1'
cstbp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.ttype == 2)])
cstbp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.ttype == 2)])
cstbp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.ttype == 2)])
cstbp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.ttype == 2)])
print("No.of system test bugs with different priorities are:",cstbp1,cstbp2,cstbp3,cstbp4)
#catbp1 stands for count of Acceptance test bugs with priority '1'
catbp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.ttype == 3)])
catbp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.ttype == 3)])
catbp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.ttype == 3)])
catbp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.ttype == 3)])
print("No.of Unit test bugs with different priorities are:",catbp1,catbp2,catbp3,catbp4)
#igtt stands for Info of test type attribute
igtt1 = (float(nut)/float(tnor))*((-1*float(cutbp1)/float(nut)*math.log(float(cutbp1)/float(nut),2))- (float(cutbp2)/float(nut)*math.log(float(cutbp2)/float(nut),2)) \
-(float(cutbp3)/float(nut)*math.log(float(cutbp3)/float(nut),2))- (float(cutbp4)/float(nut)*math.log(float(cutbp4)/float(nut),2)))
igtt2 = (float(nit)/float(tnor))*((-1*float(citbp1)/float(nit)*math.log(float(citbp1)/float(nit),2))- (float(citbp2)/float(nit)*math.log(float(citbp2)/float(nit),2)) \
-(float(citbp3)/float(nit)*math.log(float(citbp3)/float(nit),2))- (float(citbp4)/float(nit)*math.log(float(citbp4)/float(nit),2)))
igtt3 = (float(nst)/float(tnor))*((-1*float(cstbp1)/float(nst)*math.log(float(cstbp1)/float(nst),2))- (float(cstbp2)/float(nst)*math.log(float(cstbp2)/float(nst),2)) \
-(float(cstbp3)/float(nst)*math.log(float(cstbp3)/float(nst),2))- (float(cstbp4)/float(nst)*math.log(float(cstbp4)/float(nst),2)))
igtt4 = (float(nat)/float(tnor))*((-1*float(catbp1)/float(nat)*math.log(float(catbp1)/float(nat),2))- (float(catbp2)/float(nat)*math.log(float(catbp2)/float(nat),2)) \
-(float(catbp3)/float(nat)*math.log(float(catbp3)/float(nat),2))- (float(catbp4)/float(nat)*math.log(float(catbp4)/float(nat),2)))
igtt = igtt1 + igtt2 + igtt3 + igtt4
print("Information gain of Test Type Attribute is:",infopr-igtt)
