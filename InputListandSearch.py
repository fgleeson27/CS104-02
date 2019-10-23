#List creation and searching
names  = []
for num in range(0,10):
    num = input("enter a name:")
    names.append(num)
print(names)

End=False
while(End==False):
    search = input("enter search name:")
    if search in names:
        print(search, "was found")
    elif search=="End":
        print("Thanks for running the program!")
        break
    else:
        print (search, "was not found")



