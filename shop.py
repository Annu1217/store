itemAvailableDict={}

ShoppingDict={}
#welcome user
userName = input("Please enter your name:")
welcomeMessage = f"Welcome to my store,{userName}"
lenWCMg=len(welcomeMessage)
print("*"*lenWCMg)
print(welcomeMessage)
print("*"*lenWCMg)
my_file = open("items_avail.txt")
#file_str= my_file.read()
#print(file_str)
file_line= my_file.readline()
itemsAvailable = my_file.readlines()
#print(itemsAvailable)
my_file.close()

#fetch items from list and add to dictionary
print("******************Items Available in our Store***********************")
for item in itemsAvailable:
    item_name = item.split()[0]
    item_price = item.split()[1]
    print(f"{item_name}:{item_price}")
    itemAvailableDict.update({item_name:int(item_price)})
#print(itemsAvailabledict)
proceedShopping=input("Do you wish to proceed(yes/no:)")
while proceedShopping.lower()=='yes':
    item_added=input("Added an item:")
    if item_added.title() in itemAvailableDict:
      item_qty=int(input("Add quantity:"))
      ShoppingDict.update({item_added:{"quantity":item_qty,
                                       "subtotal":itemAvailableDict[item_added.title()]*
                                                  item_qty}})
      print(ShoppingDict)
    else:
        print("unable to add unavailable items")
    proceedShopping =input("Do you wish to add more items (yes/no?):")
else:
    print("\n\n")
    print("*****Bill Summary*****")
    print("\n")
    print("Item  Quantity  SubTotal")
    total=0
    for key in ShoppingDict:
        print(f"{key}    {ShoppingDict[key]['quantity']} "
              f"     {ShoppingDict[key]['subtotal']}")
        total= ShoppingDict[key]['subtotal']+total
        print(f"TOTAL:{total}")
    print("************Thank You**********")

    print("Hope to see you soon!")

