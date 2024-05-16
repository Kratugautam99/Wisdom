import time
timestamp = time.strftime('%H:%M:%S')
hour = int(input("Enter hour: "))
if(hour>=6 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<18):
  print("Good Afternoon Sir!")
elif(hour>=18 and hour<24):
  print("Good Night Sir!")
elif(hour>=0 and hour<6):
  print("Sweet Dreams Sir!")
else:
  print("Invalid Input")
print("USA Time: ",timestamp)