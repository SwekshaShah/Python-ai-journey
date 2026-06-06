#Two guest sets: VIP and Regular. Find guests on both lists, only one list, total unique guests. Implement add, remove, membership check. Use all four set operations: & | - ^.
vip_guests={"Alice","Bob","Charlie","David"}
regular_guests={"Charlie","Eve","Frank","Bob"}
print("Initial VIP Guests:",vip_guests)
print("Initial Regular Guests:",regular_guests)
both=vip_guests&regular_guests
print("Guests on both lists (VIP & Regular):",both)
vip_only_guests=vip_guests-regular_guests
print("Guests only on VIP list (VIP - Regular):",vip_only_guests)
regular_only_guests=regular_guests-vip_guests
print("Guests only on Regular list (Regular - VIP):",regular_only_guests)
total_unique_guests=vip_guests|regular_guests
print("Total unique guests (VIP | Regular):",total_unique_guests)
while True:
  print("menu:1. add vip guest, 2. add regular guest, 3. remove vip guest, 4. remove regular guest, 5. check membership, 6. exit")
  choice=int(input("Enter your choice:"))
  if choice==1:
    vip_guest=input("Enter a vip guest name:")
    vip_guests.add(vip_guest)
    print("VIP Guests after adding:",vip_guests)
  elif choice==2:
    regular_guest=input("Enter a regular guest name:")
    regular_guests.add(regular_guest)
    print("Regular Guests after adding:",regular_guests)
  elif choice==3:
    vip_guest=input("Enter a vip guest name to remove:")
    vip_guests.remove(vip_guest)
    print("VIP Guests after removing:",vip_guests)
  elif choice==4:
    regular_guest=input("Enter a regular guest name to remove:")
    regular_guests.remove(regular_guest)
    print("Regular Guests after removing:",regular_guests)
  elif choice==5:
    choice1= input("Enter do u want to check vip or regular guest:")
    if choice1=="vip":
      vip_guest=input("Enter a vip guest name to check:")
      if vip_guest in vip_guests:
        print(f"{vip_guest} is a VIP guest")
      else:
        print(f"{vip_guest} is not a VIP guest")
    elif choice1=="regular":
      regular_guest=input("Enter a regular guest name to check:")
      if regular_guest in regular_guests:
        print(f"{regular_guest} is a regular guest")
      else:
        print(f"{regular_guest} is not a regular guest")
    elif choice==6:
      break
