from abc import ABCMeta,abstractmethod
import pandas as pd
import numpy as np
class brain():
   __metaclass__ = ABCMeta
   def __init__(self,span,level):
        self.name=""
        self.description=""
        self.memory=None
        self.span=span
        self.level=level


   @abstractmethod
   def getX(x):pass

   def train():pass
   @abstractmethod
   def predict()   :pass
   @abstractmethod
   def getScore():pass


class pastLooker(brain):
    name="pastLooker"
    description="look at the past most recent past sold and that predicts for future"
    def getX(it, loc):
        file1 = pd.read_csv(loc + str(it) + '.csv')
        return file1
    def train(self,itList,loc):
        temp=pd.DataFrame()
        for it in itList:
            dataset=pastLooker.getX(it.id, loc)
            decen = dataset.sort_values(self.level+[self.span],ascending=False)
            first = decen.drop_duplicates(subset=self.level, keep='first')
            first['predicted']=first['item_cnt_day_sum']
            temp=temp.append(first[self.level+['predicted']])
        self.prediction=temp
    def predict(self,dataset):
        target=dataset.set_index(self.level)
        final=target.join(self.prediction.set_index('item_id')).reset_index()
        final['predicted']=final['predicted'].fillna(0)
        return final
class modelRunner(pastLooker):
    def train(self,itList,loc):
        temp=pd.DataFrame()
        for it in itList:
            dataset=pastLooker.getX(it.id, loc)
            decen = dataset.sort_values(self.level+[self.span],ascending=False)
            first = decen.drop_duplicates(subset=self.level, keep='first')
            first['predicted']=first['item_cnt_day_sum']
            temp=temp.append(first[self.level+['predicted']])
        self.prediction=temp














