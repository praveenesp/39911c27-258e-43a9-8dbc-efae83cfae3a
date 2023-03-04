import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
def adilabad(month):
    df=pd.read_csv("Heatwaves\\datafiles\\adilabad.csv")
    df['Average of wind_speed_min (Kmph)'].fillna(value=df['Average of wind_speed_min (Kmph)'].mean(), inplace=True)
    df['Average of wind_speed_max (Kmph)'].fillna(value=df['Average of wind_speed_max (Kmph)'].mean(), inplace=True)
    df1=pd.DataFrame()
    for index, row in df.iterrows():
        if month in row['Row Labels'] :
            df1 = df1.append(row)
    df1["target"]=df1.shift(-1)["Average of temp_max (â°C)"]
    df2=df1.tail(1)
    df2.drop(['Row Labels','target'],axis=1,inplace=True)
    x=np.array(df2)
    df1=df1[df1.target.notnull()]
    predictors = df1.columns[~df1.columns.isin(["target", "Row Labels"])]
    sc=StandardScaler()
    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18)
    X=df1[predictors]
    y=df1["target"]
    X=sc.fit_transform(X)
    rf.fit(X,y)
    X=sc.fit_transform(X)
    y=rf.predict(x)[0]
    return y
def karimnagar(month):
    df=pd.read_csv("Heatwaves\\datafiles\\karimnagar.csv")
    df['Average of wind_speed_min (Kmph)'].fillna(value=df['Average of wind_speed_min (Kmph)'].mean(), inplace=True)
    df['Average of wind_speed_max (Kmph)'].fillna(value=df['Average of wind_speed_max (Kmph)'].mean(), inplace=True)
    df1=pd.DataFrame()
    for index, row in df.iterrows():
        if month in row['Row Labels'] :
            df1 = df1.append(row)
    df1["target"]=df1.shift(-1)["Average of temp_max (â°C)"]
    df2=df1.tail(1)
    df2.drop(['Row Labels','target'],axis=1,inplace=True)
    x=np.array(df2)
    df1=df1[df1.target.notnull()]
    predictors = df1.columns[~df1.columns.isin(["target", "Row Labels"])]
    sc=StandardScaler()
    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18)
    X=df1[predictors]
    y=df1["target"]
    X=sc.fit_transform(X)
    rf.fit(X,y)
    X=sc.fit_transform(X)
    y=rf.predict(x)[0]
    return y
def khammam(month):
    df=pd.read_csv("Heatwaves\\datafiles\\khamman.csv")
    df['Average of wind_speed_min (Kmph)'].fillna(value=df['Average of wind_speed_min (Kmph)'].mean(), inplace=True)
    df['Average of wind_speed_max (Kmph)'].fillna(value=df['Average of wind_speed_max (Kmph)'].mean(), inplace=True)
    df1=pd.DataFrame()
    for index, row in df.iterrows():
        if month in row['Row Labels'] :
            df1 = df1.append(row)
    df1["target"]=df1.shift(-1)["Average of temp_max (â°C)"]
    df2=df1.tail(1)
    df2.drop(['Row Labels','target'],axis=1,inplace=True)
    x=np.array(df2)
    df1=df1[df1.target.notnull()]
    predictors = df1.columns[~df1.columns.isin(["target", "Row Labels"])]
    sc=StandardScaler()
    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18)
    X=df1[predictors]
    y=df1["target"]
    X=sc.fit_transform(X)
    rf.fit(X,y)
    X=sc.fit_transform(X)
    y=rf.predict(x)[0]
    return y
def Nizamabad(month):
    df=pd.read_csv("Heatwaves\\datafiles\\Nizamabad.csv")
    df['Average of wind_speed_min (Kmph)'].fillna(value=df['Average of wind_speed_min (Kmph)'].mean(), inplace=True)
    df['Average of wind_speed_max (Kmph)'].fillna(value=df['Average of wind_speed_max (Kmph)'].mean(), inplace=True)
    df1=pd.DataFrame()
    for index, row in df.iterrows():
        if month in row['Row Labels'] :
            df1 = df1.append(row)
    df1["target"]=df1.shift(-1)["Average of temp_max (â°C)"]
    df2=df1.tail(1)
    df2.drop(['Row Labels','target'],axis=1,inplace=True)
    x=np.array(df2)
    df1=df1[df1.target.notnull()]
    predictors = df1.columns[~df1.columns.isin(["target", "Row Labels"])]
    sc=StandardScaler()
    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18)
    X=df1[predictors]
    y=df1["target"]
    X=sc.fit_transform(X)
    rf.fit(X,y)
    X=sc.fit_transform(X)
    y=rf.predict(x)[0]
    return y
def warangal(month):
    df=pd.read_csv("Heatwaves\\datafiles\\warangal.csv")
    df['Average of wind_speed_min (Kmph)'].fillna(value=df['Average of wind_speed_min (Kmph)'].mean(), inplace=True)
    df['Average of wind_speed_max (Kmph)'].fillna(value=df['Average of wind_speed_max (Kmph)'].mean(), inplace=True)
    df1=pd.DataFrame()
    for index, row in df.iterrows():
        if month in row['Row Labels'] :
            df1 = df1.append(row)
    df1["target"]=df1.shift(-1)["Average of temp_max (â°C)"]
    df2=df1.tail(1)
    df2.drop(['Row Labels','target'],axis=1,inplace=True)
    x=np.array(df2)
    df1=df1[df1.target.notnull()]
    predictors = df1.columns[~df1.columns.isin(["target", "Row Labels"])]
    sc=StandardScaler()
    rf = RandomForestRegressor(n_estimators = 300, max_features = 'sqrt', max_depth = 5, random_state = 18)
    X=df1[predictors]
    y=df1["target"]
    X=sc.fit_transform(X)
    rf.fit(X,y)
    X=sc.fit_transform(X)
    y=rf.predict(x)[0]
    return y