#IBM Asssignment 2
'''
Python code to get temperature and humidity values generated with random function to a variable
and detect an alarm in case of high temperature
'''
import random
import winsound
temperature = random.randrange(0,100)
humidity = random.randrange(0,100)
print("Temperature = ",temperature)
if(temperature>60):
    print("HIGH TEMPERATURE")
    winsound.Beep(4460, 1000)
else:
    print("NORMAL TEMPERATURE")
    
ctr=random.randint(3,8)
Dew_point=temperature-ctr
print("Dew_point = ",Dew_point)
print("Humidity = ",humidity)


