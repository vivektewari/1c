import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funcs import RMSE
import datetime
from classes import manager
path="/home/home/PycharmProjects/1c/"
span='month'
man=manager(span)
man.putRetreive(0,"/home/home/PycharmProjects/1c//derivedData/itemInfo.csv")
man.iterator("/home/home/PycharmProjects/1c//derivedData/items/" )
info=pd.read_csv("/home/home/PycharmProjects/1c//derivedData/itemInfo.csv")
obselete=info[info.obselete==0].set_index('item_id')
pathData = path+"data"
d1=pd.read_csv(pathData+"/sales_train_v2.csv", index_col=None, header=0)
val1=d1[d1.date_block_num==32]
val2=val1.groupby('item_id')['item_cnt_day'].sum().reset_index()
val=val2.loc[obselete.index]
final=val[val.date_block_num==32].join(obselete)
final['item_cnt_day_sum']=0
final['error'] = ((final["item_cnt_day"] -final['item_cnt_day_sum']) ** 2)
#final.to_csv(path + "/output/past.csv")
f = final.sort_values(by=['error'],ascending=False)
y=RMSE(final,'item_cnt_day','item_cnt_day_sum')
print(y)

