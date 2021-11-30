sandwich_orders = ["type 1", "type 1", "type 1", "type 2", "type 2"]

print("There is no more type 1")

while "type 1" in sandwich_orders:
    sandwich_orders.remove("type 1")

print(sandwich_orders)