import time
from gdx import gdx #the gdx function calls are from a gdx.py file inside the gdx folder.
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors()
gdx.start()
num = 1000
count = 0

begin = time.time()
while count < num:
    measurements = gdx.listOfListsReadValues() #returns a list of measurements from the sensors selected.
    if measurements == None: 
        break
    channel = 1 
    for meas in measurements:                                               #Traverse channels
        print("Channel", channel)
        for i in range(0, len(meas)):                                       #Traverse measurements in each channel
            if count < num:
                print(count+1, end='  ')
                print(meas[i])
                count += 1
        channel += 1
end = time.time()
final = end - begin
print("")
print(final, "is total runtime")
gdx.stop()
gdx.close()