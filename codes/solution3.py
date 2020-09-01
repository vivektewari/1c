import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcs import RMSE
import datetime
from classes import manager
loc="/home/pooja/PycharmProjects/"
path=loc+"/1c/"
span='month'

# man=manager(span)
# man.putRetreive(0,loc+"/1c//derivedData/itemInfo.csv")
# man.iterator(loc+"/1c//derivedData/items/" ,loc+"/1c/cor.csv")
info=pd.read_csv(loc+"/1c/derivedData/itemInfo.csv")
obselete=info[info.obselete!=0].set_index('item_id')
pathData = path+"data"
d1=pd.read_csv(pathData+"/sales_train_v2.csv", index_col=None, header=0,nrows=100)
val1=d1[d1.date_block_num==32]
val2=val1.groupby('item_id')['item_cnt_day'].sum().reset_index()
val=val2[obselete.index]
final=val[val.date_block_num==32].join(obselete)
final['item_cnt_day_sum']=0
final['error'] = ((final["item_cnt_day"] -final['item_cnt_day_sum']) ** 2)
#final.to_csv(path + "/output/past.csv")
f = final.sort_values(by=['error'],ascending=False)
y=RMSE(final,'item_cnt_day','item_cnt_day_sum')
print(y)

