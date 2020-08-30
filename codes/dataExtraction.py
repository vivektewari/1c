
import pandas as pd
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas.api.types import is_numeric_dtype

import glob
path="/home/home/PycharmProjects/1c/"
pathData = path+"data"
writer = pd.ExcelWriter(path+"/analysis/" +"a1.xlsx", engine='xlsxwriter')
all_files = glob.glob(pathData + "/*.csv")

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    tot=df.shape[0]
    conso=pd.DataFrame({'count':tot},index=[1])
    for col in df.columns:
        var=df[[col]]
        conso=conso.append(pd.DataFrame({'count':int(var.isnull().sum())}, index=['missing'+"_"+col]))
        conso = conso.append(pd.DataFrame({'count': int(var.nunique())}, index=['unique' + "_" + col]))
        t=pd.DataFrame({'count':var.groupby([col]).size()}).reset_index().set_index(col)
        q=t.sort_values(by='count', ascending=False).head()
        conso=conso.append(q)
        if is_numeric_dtype(var[col]):
            conso = conso.append(pd.DataFrame({'count': float(var[col].max())}, index=['max' + "_" + col]))
            conso = conso.append(pd.DataFrame({'count': float(var[col].min())}, index=['min' + "_" + col]))


    df.head().to_excel(writer, sheet_name=filename.split("/")[-1])
    conso.to_excel(writer, sheet_name=filename.split("/")[-1],startrow=10)




writer.save()
