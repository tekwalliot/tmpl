import json
import requests
import random
from datetime import datetime, timedelta
from swpsdata.models import tp_DeviceData

headers = {'Content-Type': 'text/json'}                                                                          
url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
tp = "$89DA2@Tata!45^"     

serial_no=['65119394', '65119340']                                                                                                                                                     

for i in range(len(serial_no)):
  try:
     a = tp_DeviceData.objects.values( ).get(devNo = serial_no[i])
     fardet = {
          "agencykey":tp,
          "first_Name": str(a['name']),
          "last_Name": " ",
          "gender": str(a['gender']),
          #"dob":"{}-{}-{}".format(random.randint(1970,1988),random.randint(1,12),random.randint(1,28)),
          "dob":str(a['dob']),
          "aadhar_No":a['adhaarNo'],
          "contactno": str(a['contactNo']),
          "address_1": str(a['address']),
          "address_2": str(a['address']),
          "village": str(a['village']),
          "mandal": str(a['mandal']),
          "district": str(a['district']),
          "pin_Code": str(a['pincode']),
          "purchase_Order_Number": a['poNo'],
          "longitude": str(a['longitude']),
          "latitude": str(a['latitude']),
          "deviceid": str(a['devNo']),
          "mfg": "Shakti",
          #"mfg": str(a['conMake'] ),
          "sno": str(a['devNo']) ,
          "controller_Capacity": "5HP",
          "controller_Version": "",
          "no_Of_Stages": "7",
          "type": "AC",
          "aC_Voltage": 360,
          "aC_Current": 8.97,
          "date_Of_Installation": str(a['dateInst']),
          #"installer_Name": str(a['InstName']),
          "installer_Name": "PPS Tirupathi",
          "installer_Serial_No": 123,
          #"motor_Manufacturer": str(a['pumpMfg']),
          "motor_Manufacturer": "Shakti",
          "motor_Depth": 150,
          "motor_Capacity": "5 HP",
          "controller_Motor_Distance": 20,
          "no_of_Panels_in_series": 16,
          "no_of_Panels_in_Parallal":  1,
          "panel_Wattage": 315,
          "total_Power": 5040,
          "voc": 720,
          "vmp": 592,
          "imp": 8.53, 
	     "isc": 8.97,
          "rotating_Frequency": "50 Hz",
          "controllerPowerCapacity": "4.8 KW",
          "solarDCV": 750,
          "pvModuleMake": "TPSSL",
          #"pvModuleMake": str(a['pvMake']),
     }

     data = json.dumps(fardet)
     r = requests.post(url,data=data,headers=headers, verify=False)
     print(i,r.status_code,r.text)
  except Exception as e:
       print(i,e)