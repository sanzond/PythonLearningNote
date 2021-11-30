class User():
    """关于用户的姓名信息"""

    def __init__(self, first_name, last_name = "Smith"):
        """初始化一个用户实例"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """打印用户的信息"""
        print("User's name: "+ self.first_name + ", User's last name:" + self.last_name)

    def greet_user(self):
        """对用户进行问候"""
        print("Hello!" + self.first_name.title() + " " + self.last_name)


first_name = input("请输入你的名字:")

first_user = User(first_name)
first_user.describe_user()
first_user.greet_user()