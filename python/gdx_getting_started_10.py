import sys
import time

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors()                                #Auto-selects lowest channel available in connected device
gdx.start()                                      #Start function that begins collection thread gdx.collectLoop()
count = int(0)                          
num = int(1000)                                             #Number of measurements to take
keys = gdx.getSensors()
sensNum = len(keys)  #Get total number of sensors to test dictionary against

begin = time.time()
while count < num:
    gdx.readStoreDict()                                #API that doesn't return, just takes measurements.
    for key in keys:
        if(count < num):                                            #For each key, print each individual entry per key
            print(key)
            measurements = gdx.valueReturner(key)
            for val in measurements:
                if count < num:                                   #Prevents printing out too many measurements, ie packet of 3 printing 100 measurements ends on 102
                    print(count+1, "",  val)
                count += 1 
"""  if(count < num):                                            #For a single key, print all values
        print(keys[0])
        measurements = gdx.valueReturner(keys[0])
        for val in measurements:
            if count < num:                                   #Prevents printing out too many measurements, ie packet of 3 printing 100 measurements ends on 102
                print(count+1, "",  val)
            count += 1  """

end = time.time()
final = end - begin
print("")
print(final, "is total runtime")
gdx.stop()
gdx.close()