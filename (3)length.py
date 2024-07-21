def list_length(list):
    counter=0
    for i in list:
        counter=counter+1
    return counter
li=[1,4,5,7,8]
print("list:",li)
print("length of list using navie method is:",list_length(li))
    