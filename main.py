
def check_bit(a,b):
    if a& (1<<b)!=0:
        return True
    else :
        return False
def unset(a,b):
    if check_bit(a,b):
        return a^(1<<b)
    else:
        return a
a=int(input())
b=int(input())
print(unset(a,b))