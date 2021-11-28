guests=['brother','lover','father','mother','sister']
print(guests)
print(guests[0].title()+','+"I'm happy to see you at my party!")
print(guests[1].title()+','+"I'm happy to see you at my party!")
print(guests[2].title()+','+"I'm happy to see you at my party!")
print(guests[3].title()+','+"I'm happy to see you at my party!")
print(guests[4].title()+','+"I'm happy to see you at my party!")
#缺席客人
absent_guest=guests.pop(-2)
print(absent_guest) 
#新客人
new_guest='baby' 
guests.append(new_guest)
print(guests)
print(guests[0].title()+','+"I'm happy to see you at my party!")
print(guests[1].title()+','+"I'm happy to see you at my party!")
print(guests[2].title()+','+"I'm happy to see you at my party!")
print(guests[3].title()+','+"I'm happy to see you at my party!")
print(guests[4].title()+','+"I'm happy to see you at my party!")
#在不同位置加三位客人
guests.insert(0,'liu sir')
guests.insert(3,'ma sir')
guests.append('lu sir')
print(guests)
print(guests[0].title()+','+"I'm happy to see you at my party!")
print(guests[1].title()+','+"I'm happy to see you at my party!")
print(guests[2].title()+','+"I'm happy to see you at my party!")
print(guests[3].title()+','+"I'm happy to see you at my party!")
print(guests[4].title()+','+"I'm happy to see you at my party!")
print(guests[5].title()+','+"I'm happy to see you at my party!")
#删除客人至还剩两人
first=guests.pop(-1)
print(first+','+"I'm so sorry that we can't have a party this time")
second=guests.pop(-1)
print(second+','+"I'm so sorry that we can't have a party this time")
third=guests.pop(-1)
print(third+','+"I'm so sorry that we can't have a party this time")
forth=guests.pop(-1)
print(forth+','+"I'm so sorry that we can't have a party this time")
fifth=guests.pop(-1)
print(fifth+','+"I'm so sorry that we can't have a party this time")
sixth=guests.pop(-1)
print(sixth+','+"I'm so sorry that we can't have a party this time")
#剩下两位客人
print(guests)
print(guests[0].title()+','+"Looking forward to meeting you!")
print(guests[1].title()+','+"Looking forward to meeting you!")
#删除最后两个客人，验证打印空格
del guests[0]
del guests[0]
print(guests)