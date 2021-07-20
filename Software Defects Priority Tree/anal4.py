#pip3 install decision-tree-id3
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
#nft1 stands for number of functionality bugs, where the functionality affected is <=25%
nft1 = len(bugdtls[(bugdtls.pfuncaffec >= 0) & (bugdtls.pfuncaffec <= 25)]) 
nft2 = len(bugdtls[(bugdtls.pfuncaffec >= 26) & (bugdtls.pfuncaffec <= 50)]) 
nft3 = len(bugdtls[(bugdtls.pfuncaffec >= 51) & (bugdtls.pfuncaffec <= 75)]) 
nft4 = len(bugdtls[(bugdtls.pfuncaffec >= 76) & (bugdtls.pfuncaffec <= 100)]) 
print("No.of functionality bugs with different %ges of functionality Affected are:",nft1,nft2,nft3,nft4)
#print(bugdtls['severity'].value_counts())
#cft1bp1 stands for count of functionality type 1 bugs with priority '1'
cft1bp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.pfuncaffec >= 0) & (bugdtls.pfuncaffec <= 25)])
cft1bp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.pfuncaffec >= 0) & (bugdtls.pfuncaffec <= 25)])
cft1bp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.pfuncaffec >= 0) & (bugdtls.pfuncaffec <= 25)])
cft1bp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.pfuncaffec >= 0) & (bugdtls.pfuncaffec <= 25)])
print("No.of Functionality Type 1 bugs with different priorities are:",cft1bp1,cft1bp2,cft1bp3,cft1bp4)
#cft2bp1 stands for count of functionality type 2 bugs with priority '1'
cft2bp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.pfuncaffec >= 26) & (bugdtls.pfuncaffec <= 50)])
cft2bp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.pfuncaffec >= 26) & (bugdtls.pfuncaffec <= 50)])
cft2bp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.pfuncaffec >= 26) & (bugdtls.pfuncaffec <= 50)])
cft2bp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.pfuncaffec >= 26) & (bugdtls.pfuncaffec <= 50)])
print("No.of Functionality Type 2 bugs with different priorities are:",cft2bp1,cft2bp2,cft2bp3,cft2bp4)
#cft3bp1 stands for count of functionality type 3 bugs with priority '1'
cft3bp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.pfuncaffec >= 51) & (bugdtls.pfuncaffec <= 75)])
cft3bp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.pfuncaffec >= 51) & (bugdtls.pfuncaffec <= 75)])
cft3bp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.pfuncaffec >= 51) & (bugdtls.pfuncaffec <= 75)])
cft3bp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.pfuncaffec >= 51) & (bugdtls.pfuncaffec <= 75)])
print("No.of Functionality Type 3 bugs with different priorities are:",cft3bp1,cft3bp2,cft3bp3,cft3bp4)
#cft1bp1 stands for count of functionality type 1 bugs with priority '1'
cft4bp1 = len(bugdtls[(bugdtls.priority == 1) &(bugdtls.pfuncaffec >= 76) & (bugdtls.pfuncaffec <= 100)])
cft4bp2 = len(bugdtls[(bugdtls.priority == 2) &(bugdtls.pfuncaffec >= 76) & (bugdtls.pfuncaffec <= 100)])
cft4bp3 = len(bugdtls[(bugdtls.priority == 3) &(bugdtls.pfuncaffec >= 76) & (bugdtls.pfuncaffec <= 100)])
cft4bp4 = len(bugdtls[(bugdtls.priority == 4) &(bugdtls.pfuncaffec >= 76) & (bugdtls.pfuncaffec <= 100)])
print("No.of Functionality Type 4 bugs with different priorities are:",cft4bp1,cft4bp2,cft4bp3,cft4bp4)
#igft stands for Info of functionality type attribute
igft1 = (float(nft1)/float(tnor))*((-1*float(cft1bp1)/float(nft1)*math.log(float(cft1bp1)/float(nft1),2))- (float(cft1bp2)/float(nft1)*math.log(float(cft1bp2)/float(nft1),2)) \
-(float(cft1bp3)/float(nft1)*math.log(float(cft1bp3)/float(nft1),2))- (float(cft1bp4)/float(nft1)*math.log(float(cft1bp4)/float(nft1),2)))
igft2 = (float(nft2)/float(tnor))*((-1*float(cft2bp1)/float(nft2)*math.log(float(cft2bp1)/float(nft2),2))- (float(cft2bp2)/float(nft2)*math.log(float(cft2bp2)/float(nft2),2)) \
-(float(cft2bp3)/float(nft2)*math.log(float(cft2bp3)/float(nft2),2))- (float(cft2bp4)/float(nft2)*math.log(float(cft2bp4)/float(nft2),2)))
igft3 = (float(nft3)/float(tnor))*((-1*float(cft3bp1)/float(nft3)*math.log(float(cft3bp1)/float(nft3),2))- (float(cft3bp2)/float(nft3)*math.log(float(cft3bp2)/float(nft3),2)) \
-(float(cft3bp3)/float(nft3)*math.log(float(cft3bp3)/float(nft3),2))- (float(cft3bp4)/float(nft3)*math.log(float(cft3bp4)/float(nft3),2)))
igft4 = (float(nft4)/float(tnor))*((-1*float(cft4bp1)/float(nft4)*math.log(float(cft4bp1)/float(nft4),2))- (float(cft4bp2)/float(nft4)*math.log(float(cft4bp2)/float(nft4),2)) \
-(float(cft4bp3)/float(nft4)*math.log(float(cft4bp3)/float(nft4),2))- (float(cft4bp4)/float(nft4)*math.log(float(cft4bp4)/float(nft4),2)))
igft = igft1 + igft2 + igft3 + igft4
print("Information gain of Functionality Attribute is:",infopr-igft)

