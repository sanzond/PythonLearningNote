print("输入quit可以退出")

while True:
    age = input("请输入年龄：")

    if age == "quit":
        break
    elif int(age) < 3:
        print("免费")
    elif 3 < int(age) < 12:
        print("费用未10美元")
    else:
        print("费用未15美元")
