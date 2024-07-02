import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
if(hour>4 and hour<=12):
    print("good morning")
elif(hour>12 and hour<=17):
    print("good afternoon")
elif(hour>17 and hour<=20):
    print("good evening")
else:
    print("good night")
    
    