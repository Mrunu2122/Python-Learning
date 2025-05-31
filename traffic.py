#Conditional Statement
light = input("light: ")
if(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("LOOK")
elif(light == "green"):
    print("GO")
else:
    print("light is broken")

#character numbers 
name = "Jennifer"
print(name[1:-1])

#formatted string
first = "Mrunal"
last = "Soshte"
msg = f'{first} [{last}] is a coder'
print(msg)