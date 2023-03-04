import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
def get_SO2_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 380:
        return 100 + (x - 80) * 100 / 300
    elif x <= 800:
        return 200 + (x - 380) * 100 / 420
    elif x <= 1600:
        return 300 + (x - 800) * 100 / 800
    elif x > 1600:
        return 400 + (x - 1600) * 100 / 800
    else:
        return 0
def get_NOx_subindex(x):
    if x <= 40:
        return x * 50 / 40
    elif x <= 80:
        return 50 + (x - 40) * 50 / 40
    elif x <= 180:
        return 100 + (x - 80) * 100 / 100
    elif x <= 280:
        return 200 + (x - 180) * 100 / 100
    elif x <= 400:
        return 300 + (x - 280) * 100 / 120
    elif x > 400:
        return 400 + (x - 400) * 100 / 120
    else:
        return 0
def get_PM10_subindex(x):
    if x <= 50:
        return x
    elif x <= 100:
        return x
    elif x <= 250:
        return 100 + (x - 100) * 100 / 150
    elif x <= 350:
        return 200 + (x - 250)
    elif x <= 430:
        return 300 + (x - 350) * 100 / 80
    elif x > 430:
        return 400 + (x - 430) * 100 / 80
    else:
        return 0

def month_diff(dt1,dt2):
   from datetime import datetime
   from dateutil.relativedelta import relativedelta
   date1_str = dt1
   date2_str = dt2
   date1 = datetime.strptime(dt1, '%Y-%d-%m').date()
   date2 = datetime.strptime(dt2, '%Y-%d-%m').date()
   delta = relativedelta(date2, date1)
   months_diff = delta.months + 12 * delta.years
   return months_diff
def adilabad(date):
    df=pd.read_csv("datafiles(aqi)\\Adilabad.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df1=df['PM10']
    df1=df1.to_frame()
    df2=df['NOx']
    df2=df2.to_frame()
    df3=df['SO2']
    df3=df3.to_frame()
    model1 = ARIMA(df1, order=(1,1,1))
    model1_fit = model1.fit()
    model2 = ARIMA(df2, order=(1,1,1))
    model2_fit = model2.fit()
    model3 = ARIMA(df3, order=(1,1,1))
    model3_fit = model3.fit()
    diff=month_diff('2022-01-12',date)
    PM10prediction = model1_fit.forecast(diff)
    NOxprediction = model2_fit.forecast(diff)
    SO2prediction = model3_fit.forecast(diff)
    PM10prediction = PM10prediction.to_numpy()
    NOxprediction = NOxprediction.to_numpy()
    SO2prediction = SO2prediction.to_numpy()
    PM10=get_PM10_subindex(PM10)
    NOx=get_NOx_subindex(NOx)
    SO2=get_SO2_subindex(SO2)
    AQI=max(PM10,NOx,SO2)
    return AQI
def karimnagar(date):
    df=pd.read_csv("datafiles(aqi)\\Karimnagar.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df1=df['PM10']
    df1=df1.to_frame()
    df2=df['NOx']
    df2=df2.to_frame()
    df3=df['SO2']
    df3=df3.to_frame()
    model1 = ARIMA(df1, order=(1,1,1))
    model1_fit = model1.fit()
    model2 = ARIMA(df2, order=(1,1,1))
    model2_fit = model2.fit()
    model3 = ARIMA(df3, order=(1,1,1))
    model3_fit = model3.fit()
    diff=month_diff('2022-01-12',date)
    PM10prediction = model1_fit.forecast(diff)
    NOxprediction = model2_fit.forecast(diff)
    SO2prediction = model3_fit.forecast(diff)
    PM10prediction = PM10prediction.to_numpy()
    NOxprediction = NOxprediction.to_numpy()
    SO2prediction = SO2prediction.to_numpy()
    PM10=get_PM10_subindex(PM10)
    NOx=get_NOx_subindex(NOx)
    SO2=get_SO2_subindex(SO2)
    AQI=max(PM10,NOx,SO2)
    return AQI
def khammam(date):
    df=pd.read_csv("datafiles(aqi)\\Khammam.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df1=df['PM10']
    df1=df1.to_frame()
    df2=df['NOx']
    df2=df2.to_frame()
    df3=df['SO2']
    df3=df3.to_frame()
    model1 = ARIMA(df1, order=(1,1,1))
    model1_fit = model1.fit()
    model2 = ARIMA(df2, order=(1,1,1))
    model2_fit = model2.fit()
    model3 = ARIMA(df3, order=(1,1,1))
    model3_fit = model3.fit()
    diff=month_diff('2022-01-12',date)
    PM10prediction = model1_fit.forecast(diff)
    NOxprediction = model2_fit.forecast(diff)
    SO2prediction = model3_fit.forecast(diff)
    PM10prediction = PM10prediction.to_numpy()
    NOxprediction = NOxprediction.to_numpy()
    SO2prediction = SO2prediction.to_numpy()
    PM10=get_PM10_subindex(PM10)
    NOx=get_NOx_subindex(NOx)
    SO2=get_SO2_subindex(SO2)
    AQI=max(PM10,NOx,SO2)
    return AQI
def nizamabad(date):
    df=pd.read_csv("datafiles(aqi)\\Nizamabad.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df1=df['PM10']
    df1=df1.to_frame()
    df2=df['NOx']
    df2=df2.to_frame()
    df3=df['SO2']
    df3=df3.to_frame()
    model1 = ARIMA(df1, order=(1,1,1))
    model1_fit = model1.fit()
    model2 = ARIMA(df2, order=(1,1,1))
    model2_fit = model2.fit()
    model3 = ARIMA(df3, order=(1,1,1))
    model3_fit = model3.fit()
    diff=month_diff('2022-01-12',date)
    PM10prediction = model1_fit.forecast(diff)
    NOxprediction = model2_fit.forecast(diff)
    SO2prediction = model3_fit.forecast(diff)
    PM10prediction = PM10prediction.to_numpy()
    NOxprediction = NOxprediction.to_numpy()
    SO2prediction = SO2prediction.to_numpy()
    PM10=get_PM10_subindex(PM10)
    NOx=get_NOx_subindex(NOx)
    SO2=get_SO2_subindex(SO2)
    AQI=max(PM10,NOx,SO2)
    return AQI
def warangal(date):
    df=pd.read_csv("datafiles(aqi)\\Warangal.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df1=df['PM10']
    df1=df1.to_frame()
    df2=df['NOx']
    df2=df2.to_frame()
    df3=df['SO2']
    df3=df3.to_frame()
    model1 = ARIMA(df1, order=(1,1,1))
    model1_fit = model1.fit()
    model2 = ARIMA(df2, order=(1,1,1))
    model2_fit = model2.fit()
    model3 = ARIMA(df3, order=(1,1,1))
    model3_fit = model3.fit()
    diff=month_diff('2022-01-12',date)
    PM10prediction = model1_fit.forecast(diff)
    NOxprediction = model2_fit.forecast(diff)
    SO2prediction = model3_fit.forecast(diff)
    PM10prediction = PM10prediction.to_numpy()
    NOxprediction = NOxprediction.to_numpy()
    SO2prediction = SO2prediction.to_numpy()
    PM10=get_PM10_subindex(PM10)
    NOx=get_NOx_subindex(NOx)
    SO2=get_SO2_subindex(SO2)
    AQI=max(PM10,NOx,SO2)
    return AQI
