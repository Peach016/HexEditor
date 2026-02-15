import separation

file = open(input("File: "), "rb+")
    
values = []
run = True

while run:
    cmd = input("Command: ")

    if cmd == "write":
        data = input("Hex value: ")
        values.append(data)
        print("Value successfully created!\n")
   
    elif cmd == "read":
        try:
            data = int(input("Value number: "))
            print(values[data], "\n")
        except IndexError:
            print("Value with this index does not exists!\n")
            
    elif cmd == "delete":
        try:
            data = int(input("Value number: "))
            values.pop(data)
            print("Value successfully deleted!\n")
        except IndexError:
            print("Value with this index does not exists!\n")
   
    elif cmd == "save":
        val = "".join(values)
        val = bytes.fromhex(val)
        file.write(val)
        print("Data successfully saved to file!")
        
    elif cmd == "print":
        data = bytes.hex(file.read())
        data = separation.separation(data, 2)
        print(f"\n{data}\n")
       
    elif cmd == "exit":
        run = False