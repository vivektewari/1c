def RMSE(dataset,actual,predicted):
    return (((dataset[actual]-dataset[predicted])**2).mean())**0.5
def value(dataset,target,groupVar, variableList):
    temp=dataset.groupby(groupVar)[variableList+target].sum()
    return temp.cor()
class evaluator():
    def __init__(self,dataset,target,joiner):
        self.best=dataset.set_index(joiner)[[target]]
        self.best['bPred'] = 0
        self.best['bError']=99999
        self.best['name']=''
        self.bestrmse=9999
        self.joiner=joiner
        self.target=target
    def score(self,predictedData,pred):
        final=self.best.join(predictedData.set_index(self.joiner),how="left").reset_index()
        return RMSE(final,self.target,pred)
    def updateBest(self,predictedData,pred,name):
        final = self.best.join(predictedData.set_index(self.joiner), how="inner")
        final.assign(error =lambda x:(x.actual-x.pred)**2)
        for index1 in final.index:
            if final.loc[index1, 'error'] < final.loc[index1, 'bError'] :
                final.loc[index1, 'bPred']=final.loc[index1, 'pred']
                final.loc[index1, 'name'] = name
                final.loc[index1, 'bError'] =final.loc[index1, 'error']
            elif final.loc[index1, 'error'] == final.loc[index1, 'bError']:
                final.loc[index1, 'name'] = final.loc[index1, 'name']+";"+ name
            else :pass
            score=(final['bError'].mean())**0.5
            if score <self.bestrmse: self.bestrmse=score















