# -*- coding: utf-8 -*-
import pandas as pd;
import datetime as dt;
df=pd.read_excel('C://Users//venky//Desktop//DS_PROJECT//UCI.xlsx');
#print (df);


df['duration/sec']=0;
df['region']='';
df['time/day']='';

time1=dt.datetime.strptime('01:00','%H:%M').time();
time2=dt.datetime.strptime('06:00','%H:%M').time();
time3=dt.datetime.strptime('12:00','%H:%M').time();
time4=dt.datetime.strptime('18:00','%H:%M').time();
time5=dt.datetime.strptime('0:00','%H:%M').time();  

for index,row in df.iterrows():
    if(row[7]=='minutes'):
        a=row[6]*60;
        df.set_value(index,'duration/sec',a);
    if(row[7]=='hours'):
        a=row[6]*60*60;
        df.set_value(index,'duration/sec',a);
    if(row[7]=='seconds'):
        a=row[6];
        df.set_value(index,'duration/sec',a);

for index,row in df.iterrows():       
    if(int(row[3])>=0 or int(row[3])<= 100 ):
        df.set_value(index,'NO2_Concentration','Low');    
    if(int(row[3])>100 or int(row[3])<= 200 ):
        df.set_value(index,'NO2_Concentration','Moderate');    
    if(int(row[3])>200 or int(row[3])<= 300 ):
        df.set_value(index,'NO2_Concentration','High');        
    if(int(row[3])>300 or int(row[3])<= 400 ):
        df.set_value(index,'NO2_Concentration','Extreme');
    
    
   
    if(int(row[0])>=0 & int(row[0])<= 10 ):
        df.set_value(index,'Temp','0-10');
    if(int(row[0])>10 & int(row[0])<= 20 ):
        df.set_value(index,'Temp','10-20');
    if(int(row[0])>20 & int(row[0])<= 30 ):
        df.set_value(index,'Temp','20-30');
    if(int(row[0])>30 & int(row[0])<= 45 ):
        df.set_value(index,'Temp','30-50');
    
        
    if(row[4]=='CT' or row[4]=='ME'or row[4]=='MA' or row[4]=='NH' or row[4]=='RI' or row[4]=='VT' or row[4]=='NJ' or row[4]=='NY' or row[4]=='PA'):
        df.set_value(index,'region','Northeast');        
    if(row[4]=='IL' or row[4]=='IN'or row[4]=='MI' or row[4]=='OH' or row[4]=='WI' or row[4]=='IA' or row[4]=='KS' or row[4]=='MN' or row[4]=='MO' or  row[4]=='NE' or row[4]=='ND' or row[4]=='SD'):
        df.set_value(index,'region','Midwest');
    if(row[4]=='DE' or row[4]=='FL'or row[4]=='GA' or row[4]=='MD' or row[4]=='NC' or row[4]=='SC' or row[4]=='VA' or row[4]=='WV' or row[4]=='AL' or row[4]=='KY' or row[4]=='TN' or row[4]=='AR' or row[4]=='LA' or row[4]=='OK' or row[4]=='TX'):
        df.set_value(index,'region','South');
    if(row[4]=='AZ' or row[4]=='CO'or row[4]=='ID' or row[4]=='MT' or row[4]=='NV' or row[4]=='NM' or row[4]=='UT' or row[4]=='WY' or row[4]=='AK' or row[4]=='CA' or row[4]=='HI' or row[4]=='OR' or row[4]=='WA'):
        df.set_value(index,'region','West');
    if(row[2]>=time1 and row[2]<=time2):
        df.set_value(index,'time/day','Night');
    if(row[2]> time2 and row[2]<=time3):
        df.set_value(index,'time/day','Morning');
    if(row[2]>time3 and row[2]<=time4):
        df.set_value(index,'time/day','Afternoon');
    if(row[2]>time4 and row[2]<=time5):
        df.set_value(index,'time/day','Evening');
        #row[13]='Evening';
        #df.loc['region',index]='EVENing';

 
#print  (df['region']);    
df.to_excel('C:/Users/venky/Desktop/check3.xlsx');
        
   # print(row[11]);
   
#print(df['new'])
#print(df.columns)
   
   
   