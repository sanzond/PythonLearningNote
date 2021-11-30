class Restaurant():
    """生成关于仓管的类"""

    def __init__(self, restaurant_information, restaurant_type):
        self.restaurant_information = restaurant_information
        self.restaurant_type = restaurant_type

    def describe(self):
        """打印关于餐馆的类型的信息"""
        print(self.restaurant_information)

    def open_restaurant(self):
        """打印关于餐馆是否开门的信息"""
        print(self.restaurant_type)


restaurant_one = Restaurant("披萨店","Open")
restaurant_one.describe()
restaurant_one.open_restaurant()