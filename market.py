#尼格模擬經營
import math
import random
import os



def clsc():
    os.system('cls' if os.name == 'nt' else 'clear')

money = 5
niggs = []

def ifint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def yesNo():
    while True:
        ans = input("yes or no:").capitalize()
        if ans == "Yes" or ans == "Y" or ans == "Yeah":
            return True
        elif ans == "No" or ans == "N" or ans == "Nah": 
            return False  
        else:
            print("???\n")
class nigger:
    def __init__ (self,name,price):
        self.name = name
        self.price =price
        
    def sell(self,name):
        global niggs
        global money
        print(f"Are you sure you want to sell {name}?")
        if yesNo():
            found = "n"
            for n in niggs:
                if n.name == name:
                    found = n
                    break
            price = found.price        
            sellPrice = int(input(f"At which price do you want to sold this nigg(The original price is {price},maximum selling price is {price * 2}):"))
            if sellPrice > price:
                if sellPrice - price <= price:
                    niggs.remove(found)
                    money += sellPrice
                    print("Nigg sold successfully")
                elif sellPrice - price > price:
                    print("Too expensive")   
            elif sellPrice == price:
                print(f"You won't earn any money selling this nigg.Are you sure you are going to sell {name}?") 
                if yesNo():
                    niggs.remove(found)
                    money += sellPrice
                    print("Nigg sold successfully")
                else:
                    print("ok")    
            else:        
                print(f"You will lose money selling this nigg.Are you sure you are going to sell {name}?") 
                if yesNo():
                    niggs.remove(found)
                    money += sellPrice
                    print("Nigg sold successfully")
                else:
                    print("ok")
        else:
            print("ok")
    def buy(self,name,price):
        global money
        global niggs
        if yesNo():
                if money >= price:
                    niggs.append(nigger(name,price))
                    money -= price
                    print("Nigg bought successfully")
                else:
                    print("You don't have money to buy him")    
        else:
                print("ok")
               
 
ctn = nigger("jak",5)

def buyNigg():        
    global niggs
    global money
    createName = input("Name of nigger you want to buy:")
    chek = False
    for n in niggs:
        if n.name == createName:
            chek = True
            break
    if chek:
        print("You already have this nigg")
    else:
        pric = random.randint(1,money)
        print(f"The price of this nigg is ${pric}.Do you want to buy it?")
        ctn.buy(createName,pric)
def sellNigg():
    global niggs
    chek = False
    sellName = input("Name of nigger you want to sell:")  
    for n in niggs:
        if n.name == sellName:
            chek = True
            break
    if chek:
        ctn.sell(sellName)
    else:
        print(f"You don't have the nigg \"{sellName}\".")    
 
menu = 0
def quity(choices,typey):
    global menu
    while True:    
        if typey == "quit":
            chc = input(f"\n請輸入\"{choices}\"以退出:")
        elif typey == "choose":
            chc = input(f"請輸入序號:")
        if ifint(chc):   
            chc = int(chc)
            for i in choices:
                if chc == i:
                    return chc
                print("???\n")        
        else:       
            print("???\n")
                    
while True:    
    clsc()    
    if menu == 0:
        print("尼格模擬經營\n")
        print(f"money:{money}\n")
        print("1.Buy a nigg")
        print("2.Sell a nigg")
        print("3.Check your niggs\n")

        menu = quity([1,2,3],"choose")
    elif menu == 1:
        buyNigg() 
        quity([1],"quit")
        menu = 0
    elif menu == 2:
        sellNigg()    
        quity([1],"quit")
        menu = 0
    elif menu == 3:
        for n in niggs:
            print(f"{n.name}:${n.price}")
        quity([1],"quit")
        menu = 0