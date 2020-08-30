import pandas as pd
path="/home/home/PycharmProjects/1c/"
pathData = path+"data"
# items = pd.read_csv(pathData + "/items.csv")
# itemsCat=pd.DataFrame({'totItems':items.groupby("item_category_id").count()["item_id"]}).reset_index()
#itemsCat.to_csv(path+"/analysis/" +"catItems.csv")
h=0
train=pd.read_csv(path+"/derivedData/" +"train.csv", index_col=None, header=0)
# t1=train.groupby(["shop_id",'week','item_category_id','item_id'])['item_cnt_week'].sum().reset_index()
# t2=t1.groupby(["shop_id",'week','item_category_id'])['item_id'].count().reset_index()
# t3=t2.groupby(["shop_id",'week'])['item_category_id'].count().reset_index()
# t1.to_csv(path+"/analysis/" +"sold1.csv")
#t2.to_csv(path+"/analysis/" +"item1.csv")
#t3.to_csv(path+"/analysis/" +"cat1.csv")
f=train.corr()
#d1=train[train.item_id=].groupby(["week"])['festiveSeason','fromStart','fromEnd','item_cnt_week'].sum()
d2=0