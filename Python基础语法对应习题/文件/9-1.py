filename = 'guest.txt'
with open(filename, 'w') as file_object:
    names = input("please input your name:")
    file_object.write(names+"\n")
