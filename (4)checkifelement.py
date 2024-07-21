def check(list,element):
    for i in list:
        if i==element:
            return True
        return False
li=[9,2,34,2,5,9,16]
element=34
print("check if",element,"is in",li)
print(check(li,element))
    