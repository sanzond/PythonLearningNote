sandwich_orders = ["type 1", "type 2", "type 3"]
finished_sandwiches = []

while sandwich_orders:
    print("I made your tuna sandwich")
    finished_sandwiches.append(sandwich_orders.pop())

print(finished_sandwiches)