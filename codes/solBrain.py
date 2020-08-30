from brains import pastLooker
import pandas as pd
from funcs import evaluator
import numpy as np
import matplotlib.pyplot as plt
from funcs import RMSE
import datetime

# d1=pd.read_csv("/home/home/PycharmProjects/1c/data/sales_train_v2.csv", index_col=None, header=0)
# val1=d1[d1.date_block_num==33]
# val1=val1.groupby(['item_id']).sum().reset_index()
# val1.to_csv("/home/home/PycharmProjects/1c//derivedData/validation.csv")
val1=pd.read_csv("/home/home/PycharmProjects/1c//derivedData/validation.csv")
from classes import manager
path="/home/home/PycharmProjects/1c/"
span='month'
man=manager(span)
man.putRetreive(0,"/home/home/PycharmProjects/1c//derivedData/itemInfo.csv")

#info=pd.read_csv("/home/home/PycharmProjects/1c//derivedData/itemInfo.csv")

#past looker
s1=pastLooker('month',['item_id'])
s1.train(man.filter(list(list(val1['item_id']))),'/home/home/PycharmProjects/1c/derivedData/items/')
final=s1.predict(val1)
a=evaluator(val1,'item_cnt_day',['item_id'])
sc=a.score(final[['item_id','predicted']],'predicted')
print(sc)

