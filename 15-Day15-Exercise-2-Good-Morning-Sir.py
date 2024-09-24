import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp>=0 and timestamp<12 ):
    print("Good Morning")

elif(timestamp>=12 and timestamp<6):
    print("Good Afternoon")
else:
    print("Good Evening")