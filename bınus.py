sayilar=["1","2","3","4","5","6","7","8","9","10"]
harfler=['a','b','c',"d","e","f","g","h","i","i"]
kombin1=[]
kombin2=[]

for a in sayilar:
    for b in harfler: 
      kombin1.append(a+b)  


for c in harfler:
  for d in sayilar:
    kombin2.append(c+d) 

print("1.kombin: ",kombin1)
print("2.kombin: ",kombin2)
