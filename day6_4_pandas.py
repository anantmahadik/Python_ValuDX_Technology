# pandas is most powerfull library in the python
# it is use for data manupuluation
# install pandas and numpy (
# check pandas and nympy library and its functions and do the handson
# solve examples on pandas and numpy
# we can read specific file in panda and we can operation on specific file
#

test = {'name':['ram','sham','geeta','seeta'],
        'roll':[111,112,113,114],
        'fees':[3000,2543,1111,2222]}
import pandas as pd
df=pd.DataFrame(test,index=["aa","bb","cc","dd"])
print(df["roll"])

#print(df[1])

r=df["fees"]
mean=r.mean()
print("mean ",mean)
print(r.describe())
