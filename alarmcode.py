#IBM Asssignment 2

import random
import winsound
temperature= random.randrange(0,100)
print(temperature)
if(temperature>60):
    print("HIGH TEMPERATURE")
    winsound.Beep(4460, 1000)
else:
    print("NORMAL TEMPERATURE")
    
ctr=random.randint(3,8)
dew_point=temperature-ctr
print("dew_point = ",dew_point)
rh=100*(2.71828*(17.625*dew_point/(243.04+dew_point)))/(2.71828*(17.625*temperature/(243.04+temperature)))
print("Relative Humidity = ",round(rh,2))

