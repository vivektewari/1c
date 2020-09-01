import numpy as np
import pandas as pd

class manager():
    def __init__(self,span):

        self.span=span
        self.itemList=[]
        self.upgradeCat={}


    def getFeatures(self,dataset,varList):
        for it in self.itemList:
            t1 = dataset[dataset.item_id == it.id]
            t3 = vMaker.shiftSpan(t1, varList)
            t4 = vMaker.change(t3, t3.columns)
            t4.to_csv("/home/home/PycharmProjects/1c//derivedData/items/" + str(it.id) + ".csv")
    #def getItems(self,df):


    def addVar(self,var):
        self.varList=self.varList.add(var)
    def getCorrelation(self,dataset,target):
        temp=dataset.corr()[target:target]
        return temp

    def iterator(self,loc,file1=None):
        file1 = pd.read_csv(loc + str(0) + '.csv')
        corF=pd.DataFrame()

        for it in self.itemList:
           file1=pd.read_csv(loc+str(it.id)+'.csv')
           temp=self.getCorrelation(file1,'item_cnt_day_sum')
           temp.rename( index={'item_cnt_day_sum':it.id},inplace=True)
           temp['id'] = it.id
           temp['catagory']=it.category
           temp['count'] =len(file1)
           temp['obselete'] = it.obselete
           temp=temp[temp.columns.tolist()[-4:]+temp.columns.tolist()[:-4]]
           corF=corF.append(temp.drop(['item_id'],axis=1))
        corF.to_csv(file1)



    def makeItem(self,dataset):
        "variable Creation"
        ascen = dataset.sort_values(['item_id', self.span], ascending=True)
     
        first = ascen.drop_duplicates(subset=['item_id'], keep='first').set_index('item_id')
        last = ascen.drop_duplicates(subset=['item_id'], keep='last').set_index('item_id')
        average1=ascen.groupby(['item_id',self.span])['item_cnt_day'].sum().reset_index()
        count1 = average1.groupby(['item_id'])[self.span].count().reset_index()
        average2=average1.groupby(['item_id'])['item_cnt_day'].mean().reset_index().set_index('item_id')
        count1.set_index(['item_id'],inplace=True)
        for i in list(first.index):
                item1=(item(i))
                item1.sDate=first[self.span][i]
                item1.lDate=last[self.span][i]
                item1.sPrice=first['item_price'][i]
                item1.lPrice=last['item_price'][i]
                item1.category=first['item_category_id'][i]
                item1.name1=first['item_name'][i]
                item1.catName = first['item_category_name'][i]
                item1.averSell=average2['item_cnt_day'][i]
                item1.obselete=int(item1.lDate<30)
                item1.mnthCount = count1[self.span][i]
                self.itemList.extend([item1])
    def putRetreive(self,put,file1=None):
        'pull/put the information from/to file'
        if put==1:
            item1=pd.DataFrame(columns=['item_id','sDate','lDate','sPrice','lPrice','category','name1','catName','averSell','obselete','mnthCount'],index=range(len(self.itemList)))
            for i in range(0,len(self.itemList)):
                item1.loc[i].item_id =self.itemList[i].id
                item1.loc[i].sDate = self.itemList[i].sDate
                item1.loc[i].lDate = self.itemList[i].lDate
                item1.loc[i].sPrice = self.itemList[i].sPrice
                item1.loc[i].lPrice = self.itemList[i].lPrice
                item1.loc[i].category = self.itemList[i].category
                item1.loc[i].name1 = self.itemList[i].name1
                item1.loc[i].catName = self.itemList[i].catName
                item1.loc[i].averSell = self.itemList[i].averSell
                item1.loc[i].obselete = self.itemList[i].obselete
                item1.loc[i].mnthCount= self.itemList[i].mnthCount
            item1.to_csv(file1)
        if put==0:
            self.itemList=[]
            first=pd.read_csv(file1)
            first.set_index('item_id',inplace=True)
            for i in list(first.index):
                item1 = (item(i))
                item1.sDate = first['sDate'][i]
                item1.lDate = first['lDate'][i]
                item1.sPrice =  first['sPrice'][i]
                item1.lPrice =  first['lPrice'][i]
                item1.category = first['category'][i]
                item1.name1 = first['name1'][i]
                item1.catName = first['catName'][i]
                item1.averSell =  first['averSell'][i]
                item1.obselete = first['obselete'][i]
                item1.mnthCount=first['mnthCount'][i]
                self.itemList.extend([item1])
    def filter(self,list1):
        final=[]
        for i in range(0, len(self.itemList)):
            if self.itemList[i].id in list1:final.extend([self.itemList[i]])
        return final










class vMaker():
    def gby(self,df,gby=None,var=None,func=None):
            dvar=[]
            for v in var:
                df[v+func]=df[v]
                dvar.extend([v+func])

            d=df.groupby(dvar)[tuple(dvar)].agg(func)
    def flag(self,df,var,varValue,name):
        df[name+'flag'] = np.where(df[span] in varValue, 1, 0)
    def shiftSpan(df,varList,par=1):
        d = df[varList].shift(periods=par)
        return df.join(d,rsuffix= 'shif'+str(par))

    def change(df,varList,par=1):
        d=df[varList].diff(periods=par)
        return df.join(d,rsuffix= 'diff'+str(par))




class candidate():
    def __init__(self,id):
        #self.name=name
        self.id=id



class item():
    def __init__(self, id):
       # self.name = name
        self.id = id
        self.pred=0











