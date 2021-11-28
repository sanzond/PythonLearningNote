dic_name = {"Eric":"English", "Jobs":"French"}
dic_check_name = {}
dic_total_name = {}


print("Please enter 'end' to end taht enter")

while True:

    check_name = input(" 请输入接受审查的人员的名字: ")

    if check_name == "end":
        break
    elif check_name in dic_name:
        print("Thank you, "+ check_name + ", your favorite language is " + dic_name[check_name])
    else:
        language = input("Please enter your favorite language: ")
        dic_check_name[check_name]=language

dic_total_name.update(dic_name)
dic_total_name.update(dic_check_name)

print(dic_total_name)