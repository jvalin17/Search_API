
# coding: utf-8

# In[1]:

import json
import os
import pandas as pd

class prepData:

    def __init__ (self):
        import json
        import os
        import pandas as pd

    def getData (self, filename):
        
        dir_path = os.path.dirname(os.path.realpath('__file__'))
        filepath = dir_path + '/' + filename
        
        #reads csv file in pandas dataframe
        df = pd.read_csv(filepath)

        return df

    def renameDataframe (self, dataframe):
    
        cols = list(dataframe)
    
        new_cols = [col.replace(' ','_') for col in cols if ' ' in col]
    
    
        for i in range(len(cols)):
            if ' ' in cols[i]:
                dataframe.rename(index=str, columns={cols[i]: new_cols[i]},inplace=True)
    
        return dataframe
    

    def reduceColumns (self, dataframe):
    
        df = dataframe
    
        property_name_1 = df['Property 1 name'].unique()[0]
        property_name_2 = df['Property 2 name'].unique()[0]
    
    
        df.rename(index=str, columns={"Property 1 value": property_name_1, "Property 2 value": property_name_2},inplace=True)
    
    
        df.drop(['Property 1 name', 'Property 2 name'], axis=1, inplace=True)
    
        return df

if __name__ == "__main__":
    data_objct = prepData()
    df = data_objct.getData ('data.csv')
    df = data_objct.reduceColumns(df)
    df = data_objct.renameDataframe (df)
    df.to_csv('chem_data.csv')

