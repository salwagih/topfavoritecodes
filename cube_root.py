x = int(input("enter an integer"))
answer = 0 
while answer ** 3 < x: 
   answer = answer + 1 
if answer ** 3 != x: 
   print(str(x) + "is" + "not a perfect cube")
else: 
  print("cube root of" + str(x) + "is" + str(answer))



#ODER



x = int(input("enter an integer"))
for guess in range(x -1):
  if guess **3 == x:
    print("cube root of" + str(x) + "is" + str(guess))
    
#ich denke das die zwiete code is cleaner als die erste^^
