def swaplist(sl):
    n=len(sl)
  
    temp=sl[0]
    sl[0]=sl[n-1]
    sl[n-1]=temp

    return sl

l=[12,35,9,56,24]
print(l)
print("swapped list:",swaplist(l))
    