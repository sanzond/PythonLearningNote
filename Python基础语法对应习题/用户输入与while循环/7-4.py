print("输入quit可以退出输入")

pizzas = []

while True:

    pizza = input("请输入披萨的类型：")

    if pizza == "quit":
        break
    else:
        pizzas.append(pizza)
        print(pizzas)

print(pizzas)