#Sum up all the negative numbers in a list.

list = [1,2,-3,4,-5]
sum = 0

for i in list:
    if i<0:
        sum = sum + i

print("The sum of even numbers is {}".format(sum))