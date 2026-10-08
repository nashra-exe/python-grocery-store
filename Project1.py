def main_menu():
    while True:
        print("MAIN MENU")
        print("1. Add product")
        print("2. View cart")
        print("3. Remove product")
        print("4. Show total")
        print("5. Exit")

        choice=input("Enter your choice: ")
        choice=choice.capitalize()
        if choice== "1" or choice=="Add product":
            add_product()
        elif choice=="2" or choice=="View cart":
            view_cart()
        elif choice=="3" or choice=="Remove product":
            remove_product()
        elif choice=="4" or choice=="Show total":
            print("Your total is",total_price(),"rs")
        elif choice=="5" or choice=="Exit":
            break
        else:
            print("Invalid choice")
            
        
product_dict={
    "Apple" : 30,
    "Banana" : 20,
    "Milk" : 50,
    "Bread" : 40,
    "Eggs" : 120,
    "Ketchup" : 30}


cart=[]


def add_product():
    choice="yes"
    while choice=="yes":
        a=input("Enter a product: ")
        a=a.capitalize()
        if a in product_dict:
            cart.append(a)
            print("Added to cart")
        else:
            print("Not found")

        choice=input("Do you wish to add more products? ").lower()

                    
def view_cart():
    if len(cart)==0:
        print("Your cart is empty")
    else:
        for item in cart:
             print(item,product_dict[item])
       


def remove_product():
    i=input("Enter product to remove: ")
    i=i.capitalize()
    if i in cart:
        cart.remove(i)
        print(i,"removed from your cart")
    else:
        print("Item not found")


def total_price():
    total=0
    for item in cart:
        total+=product_dict[item]
    return total

print("========GROCERY STORE========")
print("Available Products:")
for key, value in product_dict.items():
    print(key, "-" ,value,"rs")
print("=============================")    
main_menu()
        




        








        



        
