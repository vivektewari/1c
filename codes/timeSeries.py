import pandas as pd
from funcs import RMSE
import statsmodels.api as sm
import matplotlib
path="/home/pooja/PycharmProjects/1c/"
pathData = path+"data"
writer = pd.ExcelWriter(path+"/derivedData/" +"analysis.xlsx", engine='xlsxwriter')
df1=pd.read_csv(path+"/derivedData/" +"train.csv", index_col=None, header=0)
#df1=pd.read_csv(pathData+"/sales_train_v2.csv", index_col=None, header=0)
a1=df1
a0=pd.DataFrame(a1.groupby(["shop_id","item_id"]).sum()['item_cnt_day']).reset_index()
a0['ID']=a0.index
test=a1
train=df1.drop(test.index,axis=0)
test=pd.read_csv("/home/pooja/PycharmProjects/1c/data/test.csv")
#train.to_csv(path+"/derivedData/" +"train.csv")
#writer.save()
#test=a0.drop(['item_cnt_day'],axis=1)
remaining=test
done=pd.DataFrame()
for block in range(-32,0):
    a1=df1[df1.date_block_num==-block]
    a2=a1.groupby(["shop_id","item_id"]).sum()['item_cnt_day']
    sumtemp=remaining.join(a2,on=["shop_id","item_id"])
    sliceTest=sumtemp[sumtemp.item_cnt_day.notnull()]
    remaining=remaining.drop(sliceTest.index)
    done=done.append(sliceTest)

remaining['item_cnt_day']=0
done=done.append(remaining)
done=done.sort_index()
q=int(done[["item_id"]].nunique())
w=int(test[["item_id"]].nunique())
done['item_cnt_month']=done['item_cnt_day']
done=done.drop(["shop_id","item_id", "item_cnt_day"],axis=1)
done=done.set_index('ID')
done.to_csv(path + "/output/past.csv")
final=done.join(a0[["item_cnt_day"]])
final['error'] = ((final["item_cnt_day"] -final['item_cnt_month']) ** 2)
f = final.sort_values(by=['error'],ascending=False)
y=RMSE(final,'item_cnt_day','item_cnt_month')
a=1