import numpy as np
import pandas as pd

from pandas import Series, DataFrame

address = r'C:\Users\Bidyut\Creative Cloud Files\Desktop\rawresult.csv'

rawresult = pd.read_csv(address)

rawresult.columns = ['timeStamp','elapsed','label','responseCode','responseMessage','threadName','dataType','success','failureMessage','bytes','sentBytes','grpThreads','allThreads','URL','Latency','IdleTime','Connect']
print(rawresult['timeStamp'])
rawresult1 = rawresult.loc[(rawresult['timeStamp'] >= int(1589094132855)) & (rawresult['timeStamp'] <= int(1589094405933))]
print(rawresult1)
##def calc_throughput(x):
##    return round((len(x)/((max(x)-min(x))/1000)),1)
##def calc_error(x):
##    return str(((np.size(x)-np.count_nonzero(x))/np.size(x))*100.0)+'%'
##def failedCount(x):
##    return np.size(x)-np.count_nonzero(x)
##def percentile(n):
##    def percentile_(x):
##        return np.percentile(x, n)
##    percentile_.__name__ = 'percentile_%s' % n
##    return percentile_
##label_groups=rawresult.groupby(rawresult['label']).agg(
##Samples=pd.NamedAgg(column='elapsed', aggfunc='count'),
##Average=pd.NamedAgg(column='elapsed', aggfunc=np.mean),
##Min=pd.NamedAgg(column='elapsed', aggfunc='min'),
##Max=pd.NamedAgg(column='elapsed', aggfunc='max'),
##Std=pd.NamedAgg(column='elapsed', aggfunc='std'),
##Percentile90=pd.NamedAgg(column='elapsed', aggfunc=percentile(90)),
##Percentile95=pd.NamedAgg(column='elapsed', aggfunc=percentile(95)),
##Percentile99=pd.NamedAgg(column='elapsed', aggfunc=percentile(99)),
##Median=pd.NamedAgg(column='elapsed', aggfunc='median'),
##Throughput=pd.NamedAgg(column='timeStamp', aggfunc=calc_throughput),
##Error=pd.NamedAgg(column='success', aggfunc=calc_error),
##AverageBytes=pd.NamedAgg(column='bytes', aggfunc=np.mean),
##Passed=pd.NamedAgg(column='success', aggfunc='sum'),
##Failed=pd.NamedAgg(column='success', aggfunc=failedCount),
##SentKBpersec=pd.NamedAgg(column='sentBytes', aggfunc=np.mean),
##)
##label_groups['Average'] = label_groups['Average'].astype(int)
##label_groups['AverageBytes'] = label_groups['AverageBytes'].astype(int)
##label_groups['Passed'] = label_groups['Passed'].astype(int)
##label_groups['ReceivedKB/Sec'] = round((label_groups['Throughput']*label_groups['AverageBytes'])/1024,1)
##label_groups['SentKBpersec'] = round(label_groups['SentKBpersec']/1024,1)
##
##label_groups.to_csv('AggregateRport.csv', encoding='utf-8')
