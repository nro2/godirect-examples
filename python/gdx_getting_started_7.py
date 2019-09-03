'''

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

This is an example of how to print sensor date for multiple sensors
at high speeds.  It then formats the data into order by sensor.

**** This example assumes the Go Direct sensor is connected via USB.

'''


import sys
import time

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors()                                      
gdx.start()
count = int(0)                          
num = int(100)                                             #Number of measurements to take
sensNum = len(gdx.getSensors())  #Get total number of sensors to test dictionary against
finalVal = {}
period = gdx.getPeriod() / 1000
time_stamp = 0.0

begin = time.time()
while count < num:
    measurements = gdx.readValuesRetDict()                     #returns a list of measurements from the sensors selected
    for key,values in measurements.items():                                                     
        for v in values:
            finalVal.setdefault(key, []).append(v)                      #Save a copy of dictionary
    toPrint = True    
    for key,values in finalVal.items():                                     #Check if all sensors have a measurement
        if(len(finalVal[key]) == 0):
            toPrint = False
    printInd = 0    
    if (toPrint == True):                                                   #Print head of each list in dictionary
        while(toPrint == True and count < num):
            print(count+1, " ", end='')
            print("Time: " '%4.2f' % time_stamp, end='  ',)
            time_stamp += period
            for key,value in finalVal.items():
                if printInd < num:
                    if((printInd + 1) % sensNum != 0):
                        print(key, " : ", finalVal[key].pop(0), " ", end='')
                        if(len(finalVal[key]) == 0):
                            toPrint = False
                    else:
                        print(key, " : ", finalVal[key].pop(0))
                        if(len(finalVal[key]) == 0):
                            toPrint = False
                    printInd += 1
            count += 1
    else:
        time_stamp += period

end = time.time()
final = end - begin
print("")
print(final, "is total runtime")
gdx.stop()
gdx.close()