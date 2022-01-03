import pandas
import json
import requests
from datetime import datetime, timedelta
headers = {'Content-Type': 'text/json'}                                                                          
url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
cl = "$F9C4D@Central!27^"                                                                                                                                                          



tm=list()

l=['EZMCI19010383','EZMCI19010402','EZMCI19010392','EZMCI19010372','EZMCI19010410','EZMCI19010693','EZMCI19010344']   

for j in range(len(l)):
    d=pandas.read_excel("CL4.xlsx",sheet_name="Sheet"+str(j+21))
    df=d[d.columns[2:]]
    dt,t,te,tf,tpt,co=df.columns
    tm.append([int(d[te][121]),int(d[tf][121]),int(d[tpt][121])])
    print(t)
    k=l[j]
    for i in range(121):
        mdatas ={                          
                                                                 
              "deviceid": str(k),                                                                              
              "agencykey":cl,                                                                              
               "recordedDate":str(df[dt][i]).split()[0],            
               "last_Connected_Time":str(df[t][i]),                                                  
               "total_Energy":int(df[te][i]),                                                                    
              "total_Flow": float(df[tf][i]),                                            
               "total_Pump_Time":int(df[tpt][i]),                                                  
              "co2_Emmison_saved": 0
              }
        data2 = json.dumps(mdatas)
        r2 = requests.post(url = url1 , data = data2 , headers = headers)
        print(r2.text)

serial_no=l
t=tm
for k  in range(len(t)):
  try:
      mdatas = {                                                            
      "deviceid": str(serial_no[k]),
      "date":  "2019-07-01 09:"+str(k)+":15",                                                  
      "agencykey": cl,                                      
      "recordedDate": "2020-11-30 10:"+str(k)+":52",                     
      "last_Connected_Time": "2020-11-30 10:"+str(k)+":27",                          
      "total_Energy": t[k][0],                           
      "total_Flow": t[k][1],                                 
      "total_Pump_Time": t[k][2],                    
      "co2_Emmison_saved": 0}                                                            
      data2 = json.dumps(mdatas)                                            
      r2 = requests.post(url = url2 , data = data2 , headers = headers)     
      print(r2.text)
      print(data2)
  except Exception as e:
      print(e)
