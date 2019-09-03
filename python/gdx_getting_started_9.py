import sys
import time

from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
info = gdx.sensor_info()                
chan = info[0][0]
gdx.select_sensors()                                #Auto-selects lowest channel available in connected device
gdx.new_start()                                      #Start function that begins collection thread gdx.collectLoop()
count = int(0)                          
num = int(100)                                             #Number of measurements to take
sensNum = len(gdx.getSensors())  #Get total number of sensors to test dictionary against


begin = time.time()
#time.sleep(0)
while count < num:
    #print("inside while")
    time.sleep(.05)
    measurements = gdx.retValues()                       #returns a list of measurements from the sensors selected
    if measurements != None: 
        for val in measurements:
            if count < num:                                   #Prevents printing out too many measurements, ie packet of 3 printing 100 measurements ends on 102
                print(count+1, "",  val)
            count += 1
    else:
        #print("pausing again")
        time.sleep(.02)
        
end = time.time()
final = end - begin
print("")
print(final, "is total runtime")
""" gdx.collectRunning = False
gdx.collectThread.join """
print("after collect")
gdx.stop()
print("after stop")
gdx.close()
print("after close")