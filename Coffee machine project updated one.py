#!/usr/bin/env python
# coding: utf-8

# In[ ]:


coffee_1g= int(10)
name= input("\t\nMay i know your name please: \n")
print("\t\nGood Morning",name, "!!")
a=1
while a==1:
    print("\n We have \n1.Cappucino \n2.Black Coffee \n3.Cafe Latte")
    choice=int(input("\t\nEnter 1 for Cappucino \nEnter 2 for Black Coffee \nEnter 3 for Cafe Latte\n"))
    cup = int(input("\t\n We have Dine in and Take Away. Please enter 1 for Dine in and 2 for Take Away"))
    def decoc():
            if cup== 1:
                print("\n Step 1: Ground", coffee_1g * no_of_cups,"gm of Coffee Beans")
                print("\t\n Step 2: Set the grounded coffee beans under the brewing machine")
                print("\t\n Step 3: Heat the cup with warm water under the coffee machine for 8sec")
            elif cup== 2:
                print("\n Step 1: Ground", coffee_1g * no_of_cups,"gm of Coffee Beans")
                print("\t\n Step 2: Set the grounded coffee beans under the brewing machine")
                print ("\t\n Step 3: take the take away coffee cup and")
            else:
                print("Sorry wrong Input Entered")
    def plating():
            if cup== 1:
                print ("\t\n Step 7: Pour the coffee in the cup serve with two sugar packs ")
            elif cup== 2:
                print("\t\n Step 7: Pour the coffee in take away cup with the lid above and serve with two sugar packs ")   
            else:
                print("\t\nSorry wrong Input Entered")
            
    def capucino():
            print("\t\n Step 4: Press on 30ml in the coffee machine and place 2 cups to have 15ml brewed coffee each ")
            print ("\t\n Step 5: Pour Coffee Day milk as per your choice in a jar and steam it until foam comes out")
            print("\t\n Step 6: Remove the foam from the milk ")
            print("\t\n\n NOTE: If you do not remove the foam design will not appear on coffee")
        
    if choice == 1:
        no_of_cups=int(input("\t\nMay i know how many cups you would like to have? \n"))

        decoc()
        capucino()
        plating()
        print("\t\n Enjoy your Coffee ", name, "!! we are happy to serve you any time")
    elif choice == 2:
        no_of_cups=int(input("\t\nMay i know how many cups you would like to have? \n"))

        decoc()
        capucino()
        plating()
        print("\t\n Enjoy your Coffee ", name, "!! we are happy to serve you any time")
    elif choice ==3:
        no_of_cups=int(input("\t\nMay i know how many cups you would like to have? \n"))

        decoc()
        capucino()
        plating()
        print("\t\n Enjoy your Coffee ", name, "!! we are happy to serve you any time")
    else:
        other_choice=input("Would you like to have something else? ")
        new= input("May I know What would you like to have? ")
        print("\t\n Sorry we are out of service for", new)
        print("\t\nThank You ", name, " we are happy to serve you any time")
    a=int(input("Press 1 to order again, Else don't press 1\n"))


# In[ ]:




