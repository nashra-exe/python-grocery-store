product_dict={
    "Apple" : 30,
    "Banana" : 20,
    "Milk" : 50,
    "Bread" : 40}

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
                    
add_product()
print(cart)
