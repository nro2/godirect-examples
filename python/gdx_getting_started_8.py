
import sys
import time

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
info = gdx.sensor_info()                
chan = info[0][0]
gdx.select_sensors()                                #Auto-selects lowest channel available in connected device
gdx.start()
count = int(0)                          
num = int(100)                                             #Number of measurements to take
sensNum = len(gdx.getSensors())  #Get total number of sensors to test dictionary against


begin = time.time()
while count < num:
    measurements = gdx.readValuesRetLatestDict()                       #returns a list of measurements from the sensors selected
    for val in measurements:
        if count < num:                                   #Prevents printing out too many measurements, ie packet of 3 printing 100 measurements ends on 102
            print(count+1, "",  val)
        count += 1 
end = time.time()
final = end - begin
print("")
print(final, "is total runtime")
gdx.stop()
gdx.close()