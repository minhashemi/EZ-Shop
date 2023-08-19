#next phase: add GUI, DataBase, API and make EZShop an online shop:)
#a project by Amin Hashemi (@minhashemi)

cat = ["Laptop", "PC", "AirPod", "Mobile"]
shopping = [{"id": 1001, "Name": "MacBook Pro", "Category": "Laptop", "Available": 100, "Price": 25000, "Retailer": "root"}]

userdb = [{"Username": 'root', "Password": 'toor', "First Name": 'Amin', "Last Name": 'Hashemi',
        "Role": 'R', "Wallet": 1000, "History": []},
        {"Username": 'user', "Password": '1234', "First Name": 'User', "Last Name": 'Name',
        "Role": 'C', "Wallet": 50000, "History": []}]
order = ""

#main page
def mainpage():
    print("=====================")
    print("1.Sign Up")
    print("2.Login")
    print("3.Exit")
    print("=====================")
    mainOptions()

def mainOptions():
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        
        print("\n===================================================\n")
        signup()
        print("\n===================================================\n")
        mainOptions()
    elif choice == 2:
        print("\n===================================================\n")
        login()
        print("\n===================================================\n")
        mainOptions()
    elif choice == 3:
        quit()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        mainpage()
        print("\n===================================================\n")
        mainOptions()



#signup page
def usrnmget():
    usr = input("Enter Username: ")
    for user in userdb:
        if usr == user["Username"]:
            print ("sorry! Username already taken. Please choose another one.")
            usrnmget()
    return usr
def signup():
    username = usrnmget()
    

    password = input("Enter Password: ")
    f_name = input("Enter Your First Name: ")
    l_name = input("Enter Your Last Name: ")
    role = input("Enter user role [C]Customer, [R]Retailer: ").upper()
    wallet = input("Enter Initial Wallet Budget: ")

    d = [{"Username": username, "Password": password, "First Name": f_name, "Last Name": l_name,
        "Role": role, "Wallet": wallet, "History": []}]
    userdb.extend(d)
    print ("Congratulations! You registered successfully in EzShop.")
    mainpage()




def adminLoginWindow():
    print("=====================")
    print("1.Display Menu")
    print("2.Add Product")
    print("3.Remove Product")
    print("4.Products goods available")
    print("5.Category")
    print("6.Total Income")
    print("7.Profile")
    print("8.Retail History")
    print("9.Logout")
    print("=====================")


def adminDisplayMenuWindow():
    print("Id\tName\t\tCategory\tAvailable\tPrice\tRetailer")
    print("=========================================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Category"]}\t\t{d["Available"]}\t\t{d["Price"]}\t{d["Retailer"]}')

def addprod(usr, n):
    for i in range(n):
        cate = input("Enter Product category: ")
        if cate not in cat:
            print ("Sorry! No category found. Please enter a valid category")
            addprod(usr, n)
            break
        new_id = int(input("Enter id : "))
        for item in shopping:
            if new_id == item["id"]:
                print("Duplicate Product id found! Please choose another product id..")
                addprod(usr,n)
                break
        new_Name = input("Enter Name : ")
        
        new_Available = int(input("Enter Available : "))
        new_Price = int(input("Enter Price : "))
        #Ret = int(input("Enter the original price : "))
        d = [{"id": new_id, "Name": new_Name, "Category": cate, "Available": new_Available, "Price": new_Price,
              "Retailer": usr}]
        shopping.extend(d)
        adminDisplayMenuWindow()

def addproducts(usr):
    n = int(input("Enter the no.of.items need to be added : "))
    addprod(usr, n)

def removeproducts(usr):
    prodid = int(input("Enter the id need to be deleted : "))
    for item in shopping:
        if item["id"] == prodid:
            if item["Retailer"] == usr:
                numrem = int (input("How many items you want to remove? "))
                if numrem <= item["Available"]:
                    item["Available"] -= numrem
                    print ("Selected product removed successfully!")
                    break
                else:
                    print(f'Oops! There is not that much of {item["Name"]} available in stock')
                    break
            else:
                print ("You don't own this product")
                break
    else:
        print ("Product not found!")

    adminDisplayMenuWindow()


def availableproducts(usr):
    Total = 0
    print("\n")
    for d in shopping:
        if d["Retailer"] == usr:
            print(f'{d["Name"]} = {d["Available"]}')
            Total += (d["Available"])
    print("\nTotal available goods is : ", Total)


def monthlyincome(usr):
    total = 0
    for user in userdb:
        if user["Username"] == usr:
            for item in user["History"]:
                total += item[-2]
        
    print("\nTotal income is : ", total)


def logoutwindow():
    mainpage()

def categories():
    for item in cat:
        print (item)
    
def adminOptions(myusrid):
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 2:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        addproducts(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 3:
        adminDisplayMenuWindow()
        print("\n===================================================\n")
        removeproducts(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 4:
        availableproducts(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 5:
        categories()
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 6:
        monthlyincome(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 7:
        profile(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 8:
        rethistory(myusrid)
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)
    elif choice == 9:
        logoutwindow()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        adminLoginWindow()
        print("\n===================================================\n")
        adminOptions(myusrid)


def userLoginWindow():
    print("=====================\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Charge Wallet")
    print("5.History")
    print("6.Profile")
    print("7.Logout")
    print("\n======================")


def userDisplayMenuWindow():
    print("Id\tName\t\tCategory\tAvailable\tPrice\tRetailer")
    print("=========================================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Category"]}\t\t{d["Available"]}\t\t{d["Price"]}\t{d["Retailer"]}')

def user_id():
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

def placeOrder(usr):
    order_number = 100000
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))
    num = int(input("How many items you want to buy? "))

    for d in shopping:
        if d["id"] == p_id:
            pay = d["Price"] * num
            print("Id\tName\t\tCategory\tRetailer\tAmount\tCash")
            print("=========================================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Category"]}\t\t{d["Retailer"]}\t\t{num}\t{pay}')
            order = '{d["id"]}\t{d["Name"]}\t{d["Category"]}\t{d["Available"]}\t{d["Retailer]}\t\t{d["Price"]'
            
            conform = input("\nDo you want to place an order on the above shown product: Y/N ").upper()
            if conform == 'Y':
                
                
                for user in userdb:
                    if user["Username"] == usr:
                        user["Wallet"] -= pay
                        if num <= d["Available"] and user["Wallet"]>=0:
                            
                            order_number += num
                            print("Your order number is : ", order_number)
                            d["Available"] -= num
                            orde = [order_number, d["id"], d["Name"], d["Category"], num, pay, d["Retailer"]]
                            user["History"].append(orde)
                            ret_ord = [order_number, d["id"], d["Name"], d["Category"], num, pay, user["Username"]]
                            for retail in userdb:
                                if retail["Username"] == d["Retailer"]:
                                    retail["History"].append(ret_ord)
                                    retail["Wallet"] += pay
                            print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                        elif num > d["Available"]:
                            print (f'Oops! There is not that much of {d["Name"]} in stock!')
                            placeOrder(usr)
                        elif user["Wallet"] < 0:
                            print (f'Oops! You need more money to pay for selected product(s)')
                            placeOrder(usr)

            elif conform == 'N':
                print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break
    if d["id"] != p_id:
        print("\nYou have entered invalid id. Please enter valid id\n")
        #user_id()
    print("\nAvailable products : \n")
    userDisplayMenuWindow()


def cancelOrder(usr):
    order_id = int(input("Enter the order id : "))

    for user in userdb:
        if user["Username"] == usr:
            for purchase in user["History"]:

                if purchase[0] == order_id:
                    for item in shopping:
                        if item["id"] == purchase[1]:
                            item["id"] += purchase[4]
                            user["Wallet"] += purchase[5]
                            user["History"].remove(purchase)
                            for retai in userdb:
                                if retai["Username"] == purchase[-1]:
                                    retai["Wallet"] -= purchase[5]
                                    retai["History"].remove(purchase)
                            print(f'{order_id} is removed from the placed order')
        else:
            print("Order not found!")
            order_id = int(input("Enter the order id : "))
                                
def history(usr):
    for user in userdb:
        if user["Username"] == usr:
            print("Prod. ID\tName\t\tCategory\tAmount\tPrice\tOrder Number\tRetailer")
            print("=========================================================================================")
            for purchase in user["History"]:
                
                print(f'{purchase[1]}\t\t{purchase[2]}\t{purchase[3]}\t\t{purchase[4]}\t{purchase[5]}\t{purchase[0]}\t\t{purchase[-1]}')
def rethistory(usr):
    for user in userdb:
        if user["Username"] == usr:
            print("Prod. ID\tName\t\tCategory\tAmount\tPrice\tOrder Number\tBuyer")
            print("=========================================================================================")
            for purchase in user["History"]:
                
                print(f'{purchase[1]}\t\t{purchase[2]}\t{purchase[3]}\t\t{purchase[4]}\t{purchase[5]}\t{purchase[0]}\t\t{purchase[-1]}')

def profile(myusrid):

    for user in userdb:
        if user["Username"] == myusrid:
            print(f'\nUsername: {user["Username"]}\nFirst Name: {user["First Name"]}\nLast Name: {user["Last Name"]}\nRole: {user["Role"]}\nWallet Balance: {user["Wallet"]}')
            print("=============================================================")

def charge_wallet(usr):
    for user in userdb:
        if user["Username"] == usr:
            print (f'your current balance is {user["Wallet"]}')
            charge = int (input("How much do you want to charge your wallet? "))
            user["Wallet"] += charge
            print ("Account charged successfully!")

def userChoiceOptions(myusrid):
    choice = int(input("Please enter user choice : "))
    if choice == 1:
        userDisplayMenuWindow()
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 2:
        placeOrder(myusrid)
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 3:
        cancelOrder(myusrid)
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 4:
        charge_wallet(myusrid)
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 5:
        history(myusrid)
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 6:
        profile(myusrid)
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)
    elif choice == 7:
        logoutwindow()
    else:
        print("Invalid Choice. Please enter valid choice")
        print("\n===================================================\n")
        userLoginWindow()
        print("\n===================================================\n")
        userChoiceOptions(myusrid)

def usrid():
    usr_id = input("Enter Username: ")
    return usr_id
def login():
    usrnm = usrid()
    pswrd = input("Enter Password: ")
    for user in userdb:
        
        if usrnm == user["Username"] and pswrd == user["Password"]:
            if user["Role"] == 'R':
                print (f'Welcome {user["First Name"]}')
                adminLoginWindow()
                adminOptions(usrnm)
            elif user["Role"] == 'C':
                print (f'Welcome {user["First Name"]}')
                userLoginWindow()
                userChoiceOptions(usrnm)
        elif usrnm == user["Username"] and pswrd != user["Password"]:
            print("Invalid password. Please enter valid password")





mainpage()

