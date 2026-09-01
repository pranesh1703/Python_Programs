# tag("hi","pi")


def append_item(val,items=[]):
    items.append(val)
    return items

list1=append_item(10)
list2=append_item(20)
print(list1,list2)


#multiple return paths
def check (n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    return "Zero"



def stats(x,y):
    return x+y,x*y

sum_,product=stats(2,5)
print(sum_)
print(product)



#without return
def square (x):
    x*X
