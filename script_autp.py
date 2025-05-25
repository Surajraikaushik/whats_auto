#import pywhatkit

#pywhatkit.sendwhatmsg("+91 9935709273",'Test',18 ,33)

import pywhatkit
import time
phone_number = ['+91 9935709273','+91 9044836877']  # Replace with recipient's number (include country code)

for i in phone_number:
    message = "Good Morning!"
    pywhatkit.sendwhatmsg_instantly(i, message)
time.sleep(60)
print('Done ! Successfully!')
