#Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b

def compare(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1

print(compare(5,4))