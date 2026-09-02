def test():
    return 42
    print("Hello")
result=test()
print(result)



def f(a,x=[]):
    x.append(a)
    return x
print(f(1));print(f(2))


def mystery(nums):
    for n in nums:
        if n % 2 ==0:
            return n
        return "No even found"
    print(mystery([1,3,5,7]))



def outer():
    def inner():
        return "Hi"
    return inner
result=outer()
print(result)