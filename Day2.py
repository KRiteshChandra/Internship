df1=df1[df1['total_sqft']/df1['bhk']>=300]

df1=df1[df1['bhk']<=6]

df1=df1[df1['bath']<df1['bhk']+2]

sns.boxplot(x='price_per_sqft',data=df1)

q1=df1['price_per_sqft'].quantile(0.25)
q2=df1['price_per_sqft'].quantile(0.75)
iqr=q2-q1

lower=q1-0.5*iqr
upper=q2+0.5*iqr

df1=df1[(df1['price_per_sqft']>=lower)&(df1['price_per_sqft']<=upper)]

df1

sns.boxplot(x='price_per_sqft',data=df1)

df1.reset_index(inplace=True)

df1.drop(["index",'size'],axis=1,inplace=True)

df1=pd.get_dummies(df1,columns=['location'],drop_first=True,dtype=int)

scaler=StandardScaler()

Xscaled=scaler.fit_transform(df1)

X=df1.drop(['price','price_per_sqft'],axis=1)
y=df1['price']
