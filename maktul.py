kelime="lekker"   
kelime=list(kelime)     
bos=['-','-','-','-','-','-']  
hak=6  
maktul0="""
                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     |
                         |    /\\
                        ---\n      """


maktul1="""
                          ____
                         |     |
                         |     O      
                         |    /|\
                         |     |
                         |    /
                        ---\n      """
maktul2="""
                          ____
                         |     |
                         |     O      
                         |    /|\\
                         |     
                         |    
                        ---\n      """

maktul3="""
                          ____
                         |     |
                         |     O      
                         |    /|
                         |     
                         |    
                        ---\n       """


maktul4="""
                          ____
                         |     |
                         |     O        
                         |     |
                         |     
                         |    
                        ---\n      """

maktul5="""
                          ____
                         |     |
                         |     O        
                         |    
                         |     
                         |    
                        ---\n     """
maktul6="""
                          ____
                         |     |
                         |            
                         |    
                         |     
                         |    
                        ---\n      """

adamasmaca=[maktul0,maktul1,maktul2,maktul3,maktul4,maktul5,maktul6] 

while True:
  print("aanwijzing(ipuucu)---->gewoon word in nederlands zoals moooi")
  bilgi=" {0}\n{1} HAKKINIZ KALDI\n\n\n".format(adamasmaca[hak],hak)  
  print(bilgi) 
  for i in bos: 
    print(*i,end=" ")
  
  harf=input("\nharf alınız: ")  
  if harf.isalpha()!=True or len(harf)!=1:  
    print("sadece tek harf girebilirsiniz!!")
    continue  
  else:  
    if not harf in kelime:  
      hak-=1  
    else:
      for i in range(len(kelime)):  
        if kelime[i]==harf:  
          bos[i]=harf  
    
  if kelime==bos:    
    
    print(bilgi)   
    for i in bos:   
      print(*i,end=" ")
    print("\nhelal olsun")
    break 
  if hak==0:  
    print("game over")   
    print(" {}\n\t\t{} HAKKINIZ KALDI\n\n\n\t".format(adamasmaca[0],0))  
    for i in kelime:    
      print(*i,end=" ")
    break   
