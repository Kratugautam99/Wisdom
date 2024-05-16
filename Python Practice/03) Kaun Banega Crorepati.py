import sys
print("\nKBC mein aapka swagat hai:")
print("\n1. What is the capital of India?\n")
print("  A. Delhi        B. Mumbai")
print("  C. Kolkata      D. Chennai \n")
ans = input("Enter your answer: ")
if ans == "A":
  print("\nSahi jawab!, Aap 20Lakh rupees jeet gaye hai")
else:
  print("\nGalat jawab!, aapka safar yahi tha")
  sys.exit()
print("\n2. When India got Independence?\n")
print("  A. 1949        B. 1947")
print("  C. 1950        D. 1948 \n")
ans = input("Enter your answer: ")
if ans == "B":
  print("\nSahi jawab!, Aap 40Lakh rupees jeet gaye hai")
else:
  print("\nGalat jawab!, aapka safar yahi tha")
  sys.exit()
print("\n3. Who is the Prime Minister of India?")
print('''
         A. Mamta Banerjee
         B. Rahul Gandhi
         C. Narendra Modi          
         D. Arvind Kejriwal \n''')
ans = input("Enter your answer: ")
if ans == "C":
  print("\nSahi jawab!, Aap 60Lakh rupees jeet gaye hai")
else:
  print("\nGalat Jawab!, aapka safar yahi tha")
  sys.exit()
print("\n4. Who is the President of India?")
print('''
         A. Ram Nath Kovind       
         B. Pranab Mukherjee
         C. Narendra Modi
         D. Draupadi Murmu \n''')
ans = input("Enter your answer: ")
if ans == "D":
  print("\nSahi jawab!, Aap 80Lakh rupees jeet gaye hai")
else:
  print("\nGalat Jawab!, aapka safar yahi tha")
  sys.exit()
print("\n5. Who wrote the Indian National Anthem?")
print('''
          A. Rabindranath Tagore
          B. Kabir Das
          C. Jawaharlal Nehru
          D. Mahatma Gandhi \n''')
ans = input("Enter your answer: ")
if ans == "A":
  print("\nSahi jawab!, Aap 1Crore rupees jeet gaye hai")
  sys.exit()
else:
  print("\nGalat Jawab!, aapka safar yahi tha")
  sys.exit()