import pandas
import json
import requests
from datetime import datetime, timedelta
# headers = {'Content-Type': 'text/json'}                                                                          
# url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
# url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
# url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
# tp = "$89DA2@Tata!45^"                                                                                                                                                          



tm=list()

l=['1xx','2xx']   

for j in range(len(l)):
    d=pandas.read_excel("practice.xlsx",sheet_name="Sheet"+str(j+1))
    df=d[d.columns[2:]]
    dt,t,te,tf,tpt,co=df.columns
    tm.append([int(d[te][2]),int(d[tf][2]),int(d[tpt][2])])
    #print(str(df[dt][0]).split()[0])
    #print(str(df[t][0]))
    print(te)
    k=l[j]
    for i in range(2):
      try:
        mdatas1 ={                                                                             
              "deviceid": str(k),                                                                              
              "agencykey":"tp",                                                                              
              "recordedDate":str(df[dt][i]).split()[0],            
              "last_Connected_Time":str(df[t][i]),                                                  
              "total_Energy":int(df[te][i]),                                                                    
              "total_Flow": float(df[tf][i]),                                            
              "total_Pump_Time":int(df[tpt][i]),                                                  
              "co2_Emmison_saved": 0
              }
        data1 = json.dumps(mdatas1)
        print(data1)
      except Exception as e:
        print(e)
    mdatas2 ={
    "deviceid": str(k),
    "date":  str(df[dt][0]).split()[0] + " " +str(df[t][0]),                                                  
    "agencykey": "tp",                                      
    "recordedDate": str(df[dt][1]).split()[0] + " " +str(df[t][1]),                     
    "last_Connected_Time": str(df[dt][1]).split()[0] + " " +str(df[t][1]),                          
    "total_Energy": int(d[te][2]),                           
    "total_Flow": int(d[tf][2]),                                 
    "total_Pump_Time": int(d[tpt][2]),                    
    "co2_Emmison_saved": 0 }    
    data2 = json.dumps(mdatas2)
  # r2 = requests.post(url = url1 , data = data2 , headers = headers)
    print(data2)
      




# serial_no=l
# t=tm
# for k  in range(len(t)):
#   try:
#       mdatas = {                                                            
#       "deviceid": str(serial_no[k]),
#       "date":  "2019-08-15 09:"+str(k)+":21",                                                  
#       "agencykey": "tp",                                      
#       "recordedDate": "2020-12-04 10:"+str(k)+":12",                     
#       "last_Connected_Time": "2020-12-04 10:"+str(k)+":47",                          
#       "total_Energy": t[k][0],                           
#       "total_Flow": t[k][1],                                 
#       "total_Pump_Time": t[k][2],                    
#       "co2_Emmison_saved": 0}                                                            
#       data2 = json.dumps(mdatas)                                            
#       # r2 = requests.post(url = url2 , data = data2 , headers = headers)     
#       # print(r2.text)
#       print(data2)
#   except Exception as e:
#       print(e)
