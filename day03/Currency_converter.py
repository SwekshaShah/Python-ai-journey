amount_USD= int(input("Enter your amount in Us dollar:"))
currency= input("Enter current you want to change and the available curreny are nrs,eur,gbp:")
currency1= currency.upper()
if currency1== "NRS":
    money= amount_USD *154.88
elif currency1== "EUR":
    money= amount_USD *0.86
elif currency1== "GBP":
    money= amount_USD *0.74
else:
    print("please enter nrs or eur or gbp")
print(f"{amount_USD} USD = {money} {currency}")
