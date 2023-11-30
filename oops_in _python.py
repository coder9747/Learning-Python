def outer(x):
    def inner(y=0):
        if(y==0):return x
        return outer(x+y)
    return inner;
        


print(outer(5)(8)(5)());