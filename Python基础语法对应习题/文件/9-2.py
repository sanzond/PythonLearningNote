filename = 'guest.txt'
with open(filename, 'w') as file_object:
    while True:
        names = input("please input your name:")
        if names == "break":
            break
        else:
            file_object.write(names+"\n")