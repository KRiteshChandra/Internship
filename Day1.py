import pandas as pd
import seaborn as sns
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import r2_score,mean_absolute_error

df1=pd.read_csv(r'C:\Users\Admin\Desktop\MainProject\HPP\Bengaluru_House_Data.csv')

df1=df1.drop(['area_type','balcony','society','availability'], axis=1)
##we use axis to make sure that it works column by column
df1.head()

df1.isnull().sum()

df1['location']=df1['location'].fillna('Sarjapur  Road')
df1['location'].value_counts()

df1['size']=df1['size'].fillna('2 BHK')

med_bath=df1['bath'].median()
med_bath
df1['bath']=df1['bath'].fillna(med_bath)

df1['bath']=df1['bath'].astype(int)
df1['bath'].unique()

df1.drop_duplicates(inplace=True)

df1['location']=df1['location'].apply(lambda x:x.strip())

loc=df1['location'].value_counts()
loc_lthan_10=loc[loc<=10]

df1['location']=df1['location'].apply(lambda x:'others' if x in loc_lthan_10 else x)
df1['location'].value_counts()

df1['size'].value_counts()

out=[int(i.split()[0])for i in df1['size']]

df1['bhk']=out
df1

def clean_sqft (sqft):
    li=sqft.split('-')
    try:
        if len(li)==2:
            return (float(li[0])+float(li[1]))/2
        else:
            return float(li[0])
    except:
        return None
    
df1['total_sqft']=df1['total_sqft'].apply(clean_sqft)
df1['total_sqft']=df1["total_sqft"].fillna(round(df1['total_sqft'].mean()))

df1['price_per_sqft']=df1['price']*100000/df1['total_sqft']
df1
