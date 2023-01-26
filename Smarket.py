from datetime import datetime

name=input("enter name of the customer")
Phone_number=int(input("enter the phone number"))
lists='''
rice RS 60/kg
sugar Rs 50/kg
tooth paste 55/each
salt Rs 11/kg
oil 180/l
onion Rs 35/Kg
chocklet Rs 5/each
chips Rs 10/each

'''
print(lists)

price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]

items={"rice":60,"suger":50,"toothpaste":55,"salt":11,"oil":150,"onion":35,"chocklet":5,"chips":10}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item]) 
            pricelist.appand(item,quantity,items,price)
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.appand(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print(" item not available")
    else:
        print("entered number is wrong")
    inp=input(" bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","D Mart",25*"=")
            print(28*" ","Hyderabad")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","quantity",3*" ",'price',)
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'Total Amount:','Rs',totalprice)
            print("gstamount",50*" ",'RS',gst)
            print(75*"-")
            print("gst amount",50*" ",'Rs',finalamount)
            print(75*"-")
            print(50*" ","Thanks  for visiting")
            print(75*"-")













