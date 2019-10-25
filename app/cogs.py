import pandas as pd
import numpy as np
import re

class calc_cogs:

    def __init__(self,transaction_df,costing_df):
        self.transaction_df=pd.read_csv(transaction_df)
        self.costing_df=pd.read_csv(costing_df)
        self.transaction_df['Item Name']=np.where(( self.transaction_df['Item Variation'].str.contains('Large'))|( self.transaction_df['Item Variation'].str.contains('Small')), self.transaction_df['Item Name']+'('+ self.transaction_df['Item Variation'].str[0]+')', self.transaction_df['Item Name'])
    
    def add_spaces_to_words(self,arr):
        new_arr=[]
        for word in arr:
            new_arr.append(re.sub(r"(\w)([A-Z-(])", r"\1 \2",word))
        return new_arr

    def calculate(self):
        columns_transaction_df=['Item Name','Items Sold']
        self.transaction_df= self.transaction_df[columns_transaction_df]
        self.transaction_df['Item Name']=self.transaction_df['Item Name'].str.replace(' ','')
        self.costing_df['Item Name']=self.costing_df['Item Name'].str.replace(' ','')
        merged_df=pd.merge(self.transaction_df,self.costing_df,on='Item Name',how='left')
        merged_df.columns=merged_df.columns.str.replace(' ','')
        merged_df['Cost']=merged_df['Cost'].str.replace('$','').astype(float)
        merged_df['Profit']=merged_df['Profit'].str.replace('$','').astype(float)
        merged_df['ItemsSold']=merged_df['ItemsSold'].astype(float)
        merged_df['Total Cost']=merged_df['Cost']*merged_df['ItemsSold']
        merged_df['Total Profit']=merged_df['Profit']*merged_df['ItemsSold']
        return '$'+str(round(merged_df['Total Cost'].sum(),2)),'$'+str(round(merged_df['Total Profit'].sum(),2)), self.add_spaces_to_words(np.unique(np.asarray(merged_df[merged_df['Cost'].isnull()]['ItemName'])))

"""
calc=calc_cogs('C:/Users/karti/Documents/Fall 2018/Java Junction Management/Python Project/week 13th October.csv','C:/Users/karti/Documents/Fall 2018/Java Junction Management/Python Project/Java_Costing1.csv')
print(calc.calculate())
"""