import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcs import RMSE
import datetime
from classes import manager,vMaker
from sklearn.model_selection import train_test_split
path="/home/home/PycharmProjects/1c/"
#writer = pd.ExcelWriter(path+"/derivedData/" +"trainTest.xlsx", engine='xlsxwriter')

pathData = path+"data"
d1=pd.read_csv(pathData+"/sales_train_v2.csv", index_col=None, header=0)
df2=pd.read_csv(pathData+"/items.csv", index_col=None, header=0)
df3=pd.read_csv(pathData+"/item_categories.csv", index_col=None, header=0)
df4=df2.set_index('item_id').join(df3.drop('item_category_id',axis=1),on='item_category_id')
d1=d1.set_index('item_id').join(df4,on='item_id').reset_index()

#test=pd.read_csv(pathData+"/test.csv", index_col=None, header=0)

d1["date1"]=d1.date.map(lambda x: datetime.datetime.strptime(x, "%d.%m.%Y"))
minDate=d1["date1"].min()
d1["days"]=d1.date1.map(lambda x:(x - minDate).days)
d1["week"]=d1.days.map(lambda x:int(x / 7))
d1["month"]=d1.date_block_num
d1['revenue']=d1['item_cnt_day']*d1['item_price']
span='month'
d1=d1[d1.month<33]
man=manager(span)
man.makeItem(d1)
d1['festive'] = d1.apply(lambda x: 1 if (x.month % 12)==11 else 0,axis=1 )
d2=d1.groupby(['item_id',span]).agg([np.sum,pd.Series.nunique,np.mean,np.max,np.min])
d2.columns = ["_".join(v) for v in d2.columns.values]
d2=d2.reset_index()
varList=list(d2)
items=list(set(d2.item_id))
man.getFeatures(d2,varList)
man.putRetreive(1,"/home/home/PycharmProjects/1c//derivedData/itemInfo"  + ".csv")
#man.putRetreive(0,"/home/home/PycharmProjects/1c//derivedData/itemInfo"  + ".csv")



