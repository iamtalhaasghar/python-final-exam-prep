import pandas as pd
d = {'Name':['Talha','Ahmed'], 'RollNum':['100','63']}
print(d)
mydata = pd.DataFrame(data=d)
mydata = mydata.set_index('RollNum')
print(mydata)
print(mydata.Name)
