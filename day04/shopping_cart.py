cart=[]
def show__Cart():
    if not cart:
        print("Your cart is empty:")
        return

    total=0
    for item in cart:
        print(item['Name'],item['Price']) 
        total+=item["price"]  
    print(total)     
    