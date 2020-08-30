import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np


path="/home/home/PycharmProjects/1c/"
writer = pd.ExcelWriter(path+"/derivedData/" +"analysis.xlsx", engine='xlsxwriter')
train=pd.read_csv(path+"/derivedData/" +"train.csv", index_col=None, header=0)
train["week"]=train.days.map(lambda x:int(x/7)+1)
h1=pd.DataFrame({'totSales':train[train.item_category_id.isin([12])].groupby(["date_block_num",'item_category_id']).sum()['item_cnt_day']}).reset_index() #link between time and catagory
color=['red','orange','green','yellow','black','blue','purple','brown','red','orange','green','yellow','black','blue','purple','brown']
groups=[[1,2,4,5],[10,11,13,14],[18,19,21,22],[37,38,39,40],[32,33,34,35,36]]
for i in range(4,5):
        plt.clf()
        k=0
        for j in groups[i]:
                h1p1=h1[h1.item_category_id==j]
                h1p1=h1p1.rename({'totSales':str(j)},axis='columns')

                plt.plot( 'days', str(j), data=h1p1, markerfacecolor='blue', markersize=0.05, color=color[k], linewidth=1)
                plt.legend()
                plt.savefig(path+"/derivedData/"+str(i)+".png")
                k=k+1


h2=train.groupby(["days","shop_id"]).sum()['item_cnt_day']#shop sold between time and catagory
h3t1=train.keep(["item_id","date_block_num"]).sort_values(by="item_id",ascending=True)
h3a=h3t1.drop_duplicates(subset=["item_id","date_block_num"],keep='first')
h3b=h3t1.drop_duplicates(subset=["item_id","date_block_num"],keep='last')
h3=h3a.append(h3b)#is item start and become obselete


h4t1=train.drop_duplicates(subset=["shop_id","item_category_id"],keep='first')
h4t2=pd.Dataframe({"count":train.groupby(["shop_id"]).count()["item_category_id"]})
h4=h4t2.describe()# how are catagory sale is distributed by shop



