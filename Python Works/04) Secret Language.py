import string
import random
msg = str(input("Enter a Message : "))
act = (input("Enter 1 for coding and 2 for decoding : "))
b0 = msg.split(" ")

def coding(x=b0):
 nwords = []
 for word in b0:
   if len(word) >= 3:
     N = 3
     a0 = random.sample(string.ascii_letters,N)
     c0 = random.sample(string.ascii_letters,N)
     b = word[1:]+word[0]
     a = ''.join(a0)
     c = ''.join(c0)
     nword = a+b+c
     nwords.append(nword)
   else:
     nwords.append(word[::-1])
 print(" ".join(nwords))

  
def decoding(x=b0):
  nwords = [] 
  for word in b0:
    if len(word) < 3:
      nwords.append(word[::-1])
    elif len(word) > 6:
      b = word[3:-3]
      nword = b[-1]+b[:-1]
      nwords.append(nword)
    else:
      raise ValueError("The Secret Code is not valid because each secret code word is less than 3 characters or more than 6 characters")
  print(" ".join(nwords))

if act == "1":
   coding()
elif act == "2":
  decoding()
else: 
  print ( f"Invalid input, Your input is {act} but it should be 1 or 2")
