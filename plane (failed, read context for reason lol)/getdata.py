import csv
import requests
import sys
import datetime
import http.client
import json
from datetime import datetime
import pandas as pd
from meteostat import Point, Hourly
import pytz
dat_main = [["flight_duration"   , "time" ,  "depart_temp" , "depart_rhum" , "depart_prcp" , "depart_wspd" , "depart_coco" , "arrive_temp" , "arrive_rhum" , "arrive_prcp" , "arrive_wspd" , "arrive_coco" , "weekend"]]


if input("you sure you aint hittig the limit?") != "yes":
    sys.exit(0)


conn = http.client.HTTPSConnection("api.aviationstack.com")
key = "0bnooooooooooooooooo I AM NOT TELLING YOU 7"

conn.request("GET", f"/v1/flights?flight_status=cancelled&offset=3&access_key={key}&limit=1")
res = conn.getresponse()
data = res.read().decode("utf-8")
f = json.loads(data).get("data", [])
airp = pd.read_csv(r"C:\Users\thank\OneDrive\Documents\project\plane\airports.csv" , header=None , names=["1",'2','3','4','5','6','7','8','9','10','11','12','13','14'])
def getposi(airport):
    match = airp[airp["6"] == airport]
    if not match.empty:
        return match["7"].values[0], match["8"].values[0]
    return None, None
        #lattitute 7 , longtitute 8

def getwea(time , lat , long):
    try:
        if lat == None or long == None:
            print(lat , long)
            return [None] * 5
        location = Point(lat, long)
        time = time.replace(tzinfo = None ,  minute=0, second=0, microsecond=0)
        weather = Hourly(location, time, time).fetch()
        if weather.empty:
            print("No weather data :( ")
            return [None] * 5
        row = weather.iloc[0] 
        """value = {
            "temp": row["temp"],
            "rhum": row["rhum"],
            "prcp": row["prcp"],
            "wspd": row["wspd"],
            "coco": row["coco"]
        }"""
        return [row["temp"] , row["rhum"] , row["prcp"] , row["wspd"] ,row["coco"]]
    except:
        print("no data")
        return [None] * 5

def get_timezone(icao):
    match = airp[airp["6"] == icao]
    if not match.empty:
        return match["12"].values[0]  # timezone is in column 12
    return "UTC"  # fallback

for e in f:
    data = [None]*13
    stat = e["flight_status"]
    
    
    #------------time-------------------------------------------------
    
    
    depart = e["departure"]["estimated"] or e["departure"]["scheduled"]
    arrive = e["arrival"]["estimated"] or e["arrival"]["scheduled"]
    live = e["aircraft"]
    fmt = "%Y-%m-%dT%H:%M:%S%z"
    if arrive !=None and depart != None:
        t1 = datetime.strptime(depart, fmt)
        t2 = datetime.strptime(arrive, fmt)
        data[0] = dura = int((t2 - t1).total_seconds() / 60)
    else:
        continue
    print(t1)
    data[1] = t1.hour
    
    
    #-------weather--------------------------------------------------
    
    depair = e["departure"]["icao"]
    arrair = e["arrival"]["icao"]
    locde = getposi(depair)
    locar = getposi(arrair)
    lat , long = locar
    val = getwea(t1 ,  lat , long)
    if val == [None] *5:
        continue
    data[2] = float(val[0])
    data[3] = float(val[1])
    data[4] = float(val[2])
    data[5] = float(val[3])
    data[6] = float(val[4])
    lat , long = locde
    print(t2 , lat , long)
    val = getwea(t2 ,  lat , long)
    if val == [None] *5:
        continue
    data[7] = float(val[0])
    data[8] = float(val[1])
    data[9] = float(val[2])
    data[10] = float(val[3])
    data[11] = float(val[4])
    
    #----------------------------weekday------------------------
    
    timezone = get_timezone(depair)
    localt = pytz.timezone((timezone))
    ltime = t1.astimezone(localt)
    data[12] = int(ltime.weekday() >= 5)
    print(data)

"""WARNING !!!!!!"""
"""NEVER , EVER , RUN THIS CODE MORE THAN ONCE A DAY , THE API CALL LIMIT IS 100"""
"""YOU WON'T NEED YOUR DATA THIS OFTEN"""