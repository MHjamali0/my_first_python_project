#a number selected by user and computer try to guess it
#Mohammad Hossein Jamali
#1403-09-30
import random
def myGame():
    while True:
        number=int(input("enter number:"))
        if number<0:
            break
        low=1
        top=100
        gusse=random.randrange(low,top)
        count=0
        while   number!=gusse:
            count+=1
            # gusse=random.randrange(1,100)
            print(gusse)
            
            if  number>gusse:
                low=gusse
                print("your gusse is smaller than mine.",low,"~",top)
                gusse=random.randrange(low,top)
                
                
                
            elif  number<gusse:
                top=gusse
                print("your gusse is bigger than mine.",low,"~",top)
                gusse=random.randrange(low,top)
            
                
            if  number==gusse:
                break
        print("BRAVO! your gusse is correct. you success after",count,"times")
x=int(input("select 1 or 2"))
print("1-guess number by computer")
print("2-guess number by user")
if x==1:
    myGame()