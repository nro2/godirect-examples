'''

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The following example demonstrates how to measure at higher speeds.  For example, 
when collecting faster that 51 ms, the measurements come in two per packet,
so they need to be separated.  Because of this, the number of measurements
needs to be tracked instead of the number of reads.

**** This example assumes the Go Direct sensor is connected via USB.

'''


import sys
import time

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
info = gdx.sensor_info()                
chan = info[0][0]
gdx.select_sensors([chan])                                #Auto-selects lowest channel available in connected device
gdx.start()
count = int(0)                          
num = int(100)                                             #Number of measurements to take

begin = time.time()
while count < num:
    measurements = gdx.readValues()                       #returns a list of measurements from the sensors selected
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